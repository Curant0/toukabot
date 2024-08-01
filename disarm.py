import discord
from discord import Option
from discord.ext import commands
from discord.ui import View, Select
from discord.commands import SlashCommandGroup
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.messages import BaseMessage, HumanMessage
from langchain.tools import tool
from langgraph.graph import StateGraph, END
from typing import Annotated, List, Dict, Any, TypedDict, Sequence
import os
import threading
import sys
from queue import Queue
import aiohttp
import json
import glob
import openai
from langchain_core.documents import Document
import logging
from discord.ext import commands, tasks
import asyncio
import random
import traceback
import time
from mem0 import Memory
import tracemalloc
tracemalloc.start()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

members = ["Web_Searcher", "Insight_Researcher", "Personality_Agent", "generic_worker", "memory_manager_agent"]
#members=["Personality_Agent"]
# Supervisor system prompt template
supervisor_system_prompt = (
    f"You are the supervisor. Based on the user's request, "
    f"determine which agent should act next. Your options are: {', '.join(members)}. Send to the memory agent first each time. Send to the Personality_Agent ONCE and only ONCE."
    "Respond with the name of the agent or 'FINISH' if no further action is required."
)

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    },
}

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

m = Memory.from_config(config)
# Create a global queue and a worker thread
memory_queue = Queue()


MAX_LENGTH = 2000  # Discord's character limit for messages
MAX_TOKENS = 100000 #CHATgpt 3.5 turbo approximation limit
# Predefined environment names
ENVIRONMENTS = {
    "Development Environment": '1110276173717573684',  # Will store channel ID
    "Testing Environment": '1119061204493676554',
    "Antik's Place": '1264252008462815343',# Will store channel ID
}

environment_messages = {env: MessageHistory() for env in ENVIRONMENTS}


def memory_worker():
    while True:
        task = memory_queue.get()
        if task is None:
            break  # Exit signal
        func, args, kwargs = task
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Error in memory operation: {e}")
        finally:
            memory_queue.task_done()

# Start the worker thread
worker_thread = threading.Thread(target=memory_worker, daemon=True)
worker_thread.start()



# TODO: For Curanto: Checkback and implement pathlib
# Function to load .txt documents from a directory
def load_text_documents(directory):
    documents = []
    for filepath in glob.glob(f"{directory}/*.txt"):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            documents.append(Document(page_content=content))
    return documents


# Discord bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
#tree = app_commands.CommandTree(bot)


# NOTE: Curanto: I don't perceive benefit from this command.
""" get_emoji_id
    # Try to find the emoji in the guild's emojis
"""

# TODO: For curanto: Remake as util or exception. Ease readbility.
"""chunk_message(message, chunk_size=2000):
"""

# TODO: FIND END OF ASK_UNCENSORED
#@bot.slash_command(description="Ask an uncensored question")
async def ask_uncensored(interaction: discord.Interaction, query: str):
    response_text = await process_ask_uncensored_command(interaction, query)

    # TODO: make it channel specific, if outside, make a summary
    response_chunks = chunk_message(response_text)


async def process_ask_uncensored_command(interaction, query):
    ephemeral_preference = fetch_user_ephemeral_preference(interaction.user.id)
    response_data = await ask_mistral_model(query)
    return response  # Return the response text instead of sending it

# Helper function to process the response data from the mistral model.
def process_mistral_response(response_data):
    # Check if the response is streamed
    if isinstance(response_data, list):
        # Accumulate the response parts until 'done' is True
        full_response = ""
        for part in response_data:
            if 'message' in part and 'content' in part['message']:
                full_response += part['message']['content']
            if part.get('done', False):
                break
        return full_response
    else:
        return "Error: Unexpected response format."

# Asynchronous function to send the query to the Mistral model.
async def ask_mistral_model(query):
    pass

'''
@bot.slash_command(description="Select a character")
async def select(interaction: discord.Interaction):
    # Define the options for the select menu
    options = [
        discord.SelectOption(label="Character 1", description="Description for Character 1"),
        discord.SelectOption(label="Character 2", description="Description for Character 2"),
        # Add up to 25 options...
    ]
    
    # Create the select menu and add it to a new view
    select_menu = discord.ui.Select(placeholder="Select your character...", options=options)
    view = discord.ui.View()
    view.add_item(select_menu)
    
    # Respond to the interaction by sending the select menu
    await interaction.response.send_message("Choose your character:", view=view, ephemeral=True)
'''
def update_user_preference(user_id: int, ephemeral_preference: bool):
    with sqlite3.connect('token_usage.db') as conn:
        cursor = conn.cursor()
        # Insert or update the user's preference
        cursor.execute("""
            INSERT INTO user_preferences (user_id, ephemeral_preference)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET ephemeral_preference=excluded.ephemeral_preference;
        """, (user_id, ephemeral_preference))
        conn.commit()

def fetch_user_ephemeral_preference(user_id: int) -> bool:
    # Assume 'ephemeral_preference' is a column in your user table storing the preference as an integer (0 or 1)
    with sqlite3.connect('token_usage.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ephemeral_preference FROM user_preferences  WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        # If the user has a preference set, return it as a boolean. Default to False (non-ephemeral) if not set.
        return bool(result[0]) if result else False
@bot.event
async def on_message(message):  # INFO: line 941
    # Ignore messages from the bot itself
    #if message.author == bot.user:
    #    return
    
    # CHANGE: Store the message using channel ID as the key
    channel_id = str(message.channel.id)
    if channel_id not in environment_messages:
        environment_messages[channel_id] = MessageHistory()
    
    environment_messages[channel_id].add_message(
        str(message.author),
        message.author.name,
        message.content,
      #  message.created_at.isoformat()
    )

    # Check if the message is a reply to the bot
    if message.reference and message.reference.resolved.author == bot.user:
        # Get the original message (bot's message)
        original_message = await message.channel.fetch_message(message.reference.message_id)
        
        # Extract the original query and response
        original_content = original_message.content.split('\n', 1)
        original_query = original_content[0] if len(original_content) > 0 else ""
        original_response = original_content[1] if len(original_content) > 1 else ""

        # Create the combined query
        combined_query = f"Previous query: {original_query}\nPrevious response: {original_response}\nNew query: {message.content}"

        # Call handle_reply to process the reply
        await handle_reply(message)
    elif bot.user in message.mentions:
        # Remove the bot's mention from the message content
        query = message.content.replace(f'<@!{bot.user.id}>', '').replace(f'<@{bot.user.id}>', '').strip()

        # If there's any content after removing the mention, process it
        if query:
            # Create a combined query with just the new query
            combined_query = f"New query: {query}"

            # Call handle_reply to process the mention
            await handle_reply(message)

    # Process commands
    await bot.process_commands(message)

@bot.slash_command(name="set_message_preference", description="Set your message preference to ephemeral or permanent")
@discord.option("preference", description="Choose your message preference", choices=["Ephemeral", "Permanent"])
async def set_message_preference(ctx: discord.ApplicationContext, preference: str):
    # Convert the preference to a boolean value: Ephemeral=True, Permanent=False
    ephemeral_preference = True if preference == "Ephemeral" else False
    
    # Update the user's preference in the database
    update_user_preference(ctx.user.id, ephemeral_preference)
    
    # Create an embed for feedback
    embed = discord.Embed(title="Message Preference", description=f"Your message preference has been set to **{preference}**.", color=0x00ff00)
    
    # Provide feedback to the user with an embed
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="buy-more-tokens", description="Top up your token balance and support AI development")
async def buy_more_tokens(interaction: discord.Interaction):
    # Check if the channel is whitelisted
    if not is_channel_whitelisted(interaction):
        # Create an embed for the error message
        embed = discord.Embed(title="Restricted Access", description="Oh no, this channel isn't fancy enough for my tastes. Try a whitelisted one, perhaps?", color=0xff0000)
        
        # Send the embed as a response
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return  # Stop executing the command
    
    # Create an embed for the support message
    embed = discord.Embed(title="Support AI Development", description=support_message, color=0x3498db)
    
    # Respond to the command with the embed
    await interaction.response.send_message(embed=embed, ephemeral=False)

@bot.slash_command(name="help", description="Learn how to use the bot and its features")
async def help_command(interaction: discord.Interaction):
    # Create an embed for the help content
    embed = discord.Embed(title="Help Guide: Using the AI Bot", description="Learn how to use the bot and its features", color=0x3498db)
    embed.add_field(name="Selecting a Character", value="Use `/select_character <character_name>` to choose an AI persona for your interactions. Each character has a unique personality and will respond differently.", inline=False)
    embed.add_field(name="What are Tokens?", value="Tokens are currency for interaction. Each message processed by the bot costs tokens. You can check your token balance with `/balance`. Buy more tokens using `/buy-more-tokens` to support AI development and continue using the bot.", inline=False)
    embed.add_field(name="Interacting with the Bot", value="Use `/interact <your_message>` to engage with the bot in a conversation. The bot will respond based on the selected character's personality and your query.", inline=False)
    #embed.add_field(name="Uncensored Model", value="The uncensored model, accessible with `/ask_uncensored`, provides responses without content restrictions. It is designed for open-ended questions and may provide more direct answers.", inline=False)
    embed.set_footer(text="For more information or assistance, contact the bot developer, Womp Womp.")
    
    ephemeral_preference = fetch_user_ephemeral_preference(interaction.user.id)
    
    # Send the help content as an embed, respecting the user's ephemeral preference
    await interaction.response.send_message(embed=embed, ephemeral=ephemeral_preference)

# Check balance and suggest 'Buy Me a Coffee' if the balance is low
@bot.slash_command(description="Check your balance and top up if needed")
async def balance(interaction: discord.Interaction):
    #    Check if the channel is whitelisted
    if not is_channel_whitelisted(interaction):
        await interaction.response.send_message("Oh no, this channel isn't fancy enough for my tastes. Try a whitelisted one, perhaps?", ephemeral=True)
        return  # Stop executing the command
    user_id = interaction.user.id
    balance = get_balance(user_id)
    ephemeral_preference = fetch_user_ephemeral_preference(interaction.user.id)
    if balance is None:
        add_new_user(user_id)
        balance = 1.00  # Initial balance for new users

    if balance <= 0.10:  # If balance is low, suggest topping up
        await interaction.response.send_message(
            f"Your current balance is low: ${balance:.2f}. {support_message}", 
            ephemeral=ephemeral_preference
        )
    else:
        await interaction.response.send_message(
            f"Your current balance is: ${balance:.2f}. Feel free to top up anytime! {support_message}", 
            ephemeral=ephemeral_preference
        )
async def character_autocomplete(ctx: discord.AutocompleteContext):
    return [character for character in character_prompts if ctx.value.lower() in character.lower()]

@bot.slash_command(name="select_character", description="Select a character")
@discord.option("character", description="Choose your character", autocomplete=character_autocomplete)
async def select_character(ctx: discord.ApplicationContext, character: str):
    # Check if the channel is whitelisted
    if not is_channel_whitelisted(ctx):
        # Create an embed for the error message
        embed = discord.Embed(title="Restricted Access", description="Oh no, this channel isn't fancy enough for my tastes. Try a whitelisted one, perhaps?", color=0xff0000)
        
        # Send the embed as a response
        await ctx.respond(embed=embed, ephemeral=True)
        return  # Stop executing the command

    user_id = ctx.user.id  # Get the user's ID
    user_selected_characters[user_id] = character  # Save the selected character
    ephemeral_preference = fetch_user_ephemeral_preference(user_id)

    # Debug line
    print(f"Character selected by {ctx.user}: {character}")

    # Create an embed for the character selection confirmation
    embed = discord.Embed(title="Character Selection", description=f"You selected **{character}**.", color=0x00ff00)
    
    # Send the embed as a response, respecting the user's ephemeral preference
    await ctx.respond(embed=embed, ephemeral=ephemeral_preference)


@bot.slash_command(description="Interact with the AI agent") # INFO: line 1267
async def interact(interaction: discord.Interaction, query: str):
    # Acknowledge the interaction immediately and defer the actual response):
    # Acknowledge the interaction immediately and defer the actual response
    if not is_channel_whitelisted(interaction):
        await interaction.response.send_message("Oh no, this channel isn't fancy enough for my tastes. Try a whitelisted one, perhaps?", ephemeral=True)
        return  # Stop executing the command
    
    ephemeral_preference = fetch_user_ephemeral_preference(interaction.user.id)
    await interaction.response.defer(ephemeral=ephemeral_preference)
    print(f"Received query from {interaction.user}: {query}")
    
    # Initialize token tracking
    total_tokens_used = count_tokens(query)  # Start with tokens from the user's query

    user_id = interaction.user.id
    balance = get_balance(user_id)
    
    # Check if the user exists in the database
    if balance is None:
        add_new_user(user_id)
        balance = 1.00  # Assuming you start new users with $1.00
        
    # Check if the balance is sufficient
    if balance <= 0:
        await interaction.response.send_message("You do not have enough balance to use this command.", ephemeral=True)
        return

    # Fetch the last 10 messages from the channel
    #channel = interaction.channel
    #last_messages = []
    #async for message in channel.history(limit=10):
    #    message_data = {
    #        "author": str(message.author),
    #        "username": message.author.name,
    #        "content": message.content,
    #        "timestamp": message.created_at.isoformat()
    #    }
    #    last_messages.append(message_data)
    #last_messages.reverse()  # Most recent last
        # CHANGE: Get stored messages for the current channel

    # CHANGE: Get stored messages for the current channel
    channel_id = str(interaction.channel.id)
    print(channel_id)
    if channel_id not in environment_messages:
        environment_messages[channel_id] = MessageHistory()
    # Add the current query to the messages
    environment_messages[channel_id].add_message(
        str(interaction.user),
        interaction.user.name,
        query,
       # interaction.created_at.isoformat()
    )

    # Get the last 10 messages in a formatted string
    stored_messages = environment_messages[channel_id].read(10)
    print("-----------------------------------------------------------")
    print(stored_messages)
    print(f"New query: {query}")

    # Fetch the selected character for the user or default Touka: "Touka"
    character_name = user_selected_characters.get(user_id, "Touka")
    # Use the selected character or default to "Touka"
    #character_name = character or "Touka"
    
    # Fetch the system prompt for the selected character or default prompt
    system_prompt = character_prompts.get(character_name, "You are Toukabot, a helpful AI Assistant. Take input text and output it with added flair, sass, zest, and sexiness! And any additional analysis, of course.")

    try:
        # Call the AI conversation function
        response = ai_conversation(stored_messages, character_name, system_prompt, tools, interaction.channel.id)
        
        # Count tokens in the response
        total_tokens_used += count_tokens(response)

        # Calculate interaction cost and update balance
        interaction_cost = calculate_cost(total_tokens_used)
        update_balance(user_id, interaction_cost)
        new_balance = balance - interaction_cost
        
        # Create a plain text response
        response_text = f"{response}\n\n"
        response_text += f"Tokens: {total_tokens_used}; Used: ${interaction_cost:.4f}; Owned: ${new_balance:.4f}"
        
        # Send the plain text response
        await interaction.followup.send(response_text, ephemeral=ephemeral_preference)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        error_message = f"An error occurred while processing your request: {str(e)}"
        await interaction.followup.send(error_message, ephemeral=ephemeral_preference)
# Make sure to add the following tools to your tools list:
# tools.extend([set_sleep, get_sleep])
#bot.add_view(ReplyView(bot, interact))

async def handle_reply(message):
    # Get the original message (bot's message)
    original_message = await message.channel.fetch_message(message.reference.message_id)
    
    # Extract the original query and response
    original_content = original_message.content.split('\n', 1)
    #character_name = original_content[0].split(' says:')[0] if len(original_content) > 0 else "Unknown"
    original_response = original_content[1] if len(original_content) > 1 else ""

    # Create the combined query
    combined_query = f"Previous response: {original_response}\nNew query: {message.content}"

    # Initialize token tracking
    total_tokens_used = count_tokens(combined_query)

    user_id = message.author.id
    balance = get_balance(user_id)
    
    # Check if the user exists in the database
    if balance is None:
        add_new_user(user_id)
        balance = 1.00  # Assuming you start new users with $1.00

    # Check if the balance is sufficient
    if balance <= 0:
        await message.channel.send("You do not have enough balance to continue this conversation.", reference=message)
        return

    # Fetch the selected character for the user or default to the one used in the original message
    character_name = user_selected_characters.get(user_id)

    # Fetch the system prompt for the selected character or default prompt
    system_prompt = character_prompts.get(character_name, "You are KirinBot, a helpful AI Assistant. Take input text and output it with added flair, sass, zest, and sexiness! And any additional analysis, of course.")
    
    try:
        # CHANGE: Get stored messages for the current channel
        channel_id = str(message.channel.id)
        if channel_id not in environment_messages:
            environment_messages[channel_id] = MessageHistory()
        # Add the current query to the messages
        #environment_messages[channel_id].add_message(
        #    str(message.author),
        #    message.author.name,
        #    message.content,
        ## interaction.created_at.isoformat()
        #)
    
        # Get the last 10 messages in a formatted string
        stored_messages = environment_messages[channel_id].read(10)
        print("--------------------------stored_messages---------------------------------")
        print(stored_messages)
        print(f"New query: {stored_messages}")

        # Call the AI conversation function
        response = ai_conversation(stored_messages, character_name, system_prompt, tools, message.channel.id)
        
        # Count tokens in the response
        total_tokens_used += count_tokens(response)

        # Calculate interaction cost and update balance
        interaction_cost = calculate_cost(total_tokens_used)
        update_balance(user_id, interaction_cost)
        new_balance = balance - interaction_cost
        
        # Create a plain text response
        response_text = f"{response}\n\n"
        response_text += f"Tokens: {total_tokens_used}; Spent: ${interaction_cost:.4f}; Owned: ${new_balance:.4f}"
        
        # Send the response as a reply to the user's message
        await message.reply(response_text)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Create an embed for the error message
        error_embed = discord.Embed(title="Error", description="An error occurred while processing your request.", color=0xff0000)
        await channel.send(embed=error_embed)
@commands.command()
async def verify_ai_cog(self, ctx):
    await ctx.send("AutonomousAIConversation cog is active!")
    logger.info("Verify command was called")
    
def ai_conversation(last_messages: List[Dict[str, str]], character_name: str, system_prompt: str, tools: List, channel_id: str):
    # Initialize the dynamic StateGraph for this interaction
    print(channel_id)
    dynamic_workflow = StateGraph(AgentState)
    print("    dynamic_workflow = StateGraph(AgentState)")
    # Create the dynamic agent based on the selected character's prompt
    personality_agent = create_agent(llm, tools, system_prompt)
    print(" personality_agent = create_agent(llm, tools, system_prompt)")
    # Initialize the dynamic StateGraph for this interaction
    dynamic_workflow = StateGraph(AgentState)
    dynamic_workflow.add_node("Web_Searcher", lambda state: agent_node(state, web_searcher_agent, "Web_Searcher"))
    dynamic_workflow.add_node("Insight_Researcher", lambda state: agent_node(state, insight_researcher_agent, "Insight_Researcher"))
    dynamic_workflow.add_node("generic_worker", lambda state: agent_node(state, generic_worker_agent, "generic_worker"))
    dynamic_workflow.add_node("Personality_Agent", lambda state: agent_node(state, personality_agent, character_name))
    dynamic_workflow.add_node("memory_manager_agent", lambda state: agent_node(state, memory_manager_agent, "memory_manager_agent"))
    dynamic_workflow.add_node("supervisor", supervisor_chain)

    # Define edges from each agent back to the supervisor
    dynamic_workflow.add_edge("generic_worker", "supervisor")
    dynamic_workflow.add_edge("Web_Searcher", "supervisor")
    dynamic_workflow.add_edge("Insight_Researcher", "supervisor")
    dynamic_workflow.add_edge("memory_manager_agent", "supervisor")
    dynamic_workflow.add_edge("Personality_Agent", END)

    # Update the conditional edges
    conditional_map = {k: k for k in members}
    conditional_map["FINISH"] = END
    dynamic_workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)

    # Set the entry point
    dynamic_workflow.set_entry_point("supervisor")
    
    # Compile the graph
    compiled_dynamic_graph = dynamic_workflow.compile()
   
   #combined_messages = stored_messages[-10:]  # Get last 10 stored messages
    #async for message in interaction.channel.history(limit=10):
    #    message_data = {
    #        "author": str(message.author),
    #        "username": message.author.name,
    #        "content": message.content,
    #        "timestamp": message.created_at.isoformat()
    #    }
    #    if message_data not in combined_messages:
    #        combined_messages.append(message_data)
    #

    print("------------------------------------------------------")
    print(last_messages)
    
    query = f"""{last_messages}
    ||System Message: This message here is the one you should directly reply to||
    """
    
    input_data = {"messages": [HumanMessage(content=query)]}
    print("-------------------------input data-----------------------------")
    print(input_data)
    
    # Process the query through the graph
    last_output = None
    for output in compiled_dynamic_graph.stream(input_data, stream_mode="updates"):
        last_output = output
        print("--------------------------last output----------------------------")
        print(last_output)
        if output.get("agent", {}).get("state") != "terminal":
            for key, value in output.items():
                if key != "supervisor":
                    latest_message_content = value["messages"][-1].content
                    print("-----------------------latest_message_contet-------------------------------")
                    print(latest_message_content)
                    if latest_message_content != query:
                        input_data["messages"].append(value["messages"][-1])
    
    # Extract the final message
    final_message = None
    if last_output:
        for key, value in last_output.items():
            if isinstance(value, dict) and "messages" in value:
                final_message = value["messages"][-1]
                print(final_message)
                channel_id = str(channel_id)
                if channel_id not in environment_messages:
                    environment_messages[channel_id] = MessageHistory()

                        # Add the current query to the messages
                environment_messages[channel_id].add_message(
                    character_name,
                    character_name,
                    final_message,
                 #interaction.created_at.isoformat()
                )
    
                break
    
    return final_message.content if final_message else "No response generated."


# Assuming you have these functions/variables defined elsewhere
# from your_module import ai_conversation, read_last_50_messages, get_sleep, set_sleep, character_prompts, tools, send_message



def setup(bot):
    try:
        bot.add_cog(AutonomousAIConversation(bot))
        logger.info("AutonomousAIConversation cog added successfully")
    except Exception as e:
        logger.error(f"Error adding AutonomousAIConversation cog: {e}")
        logger.error(traceback.format_exc())

async def load_extensions():
    try:
        #await bot.load_extension("AutonomousAIConversation")
        print("Successfully loaded autonomous_ai_conversation")
    except Exception as e:
        print(f"Failed to load extension autonomous_ai_conversation. Error: {e}")


 #f"Your query: {query}\n\n"
 
async def main():
    async with bot:
        
        await bot.start(os.environ.get("DISCORD_BOT_TOKEN"))
        await bot.add_cog(AutonomousAIConversation(bot))
        print("start")
if __name__ == "__main__":
    asyncio.run(main())
