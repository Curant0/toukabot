import logging
from discord.ext import commands, tasks
import asyncio
import random
import traceback
import time

# Import your necessary functions and variables
from main2 import ai_conversation, read_last_50_messages, get_sleep, set_sleep, character_prompts, tools, send_message, global_sleep

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AutonomousAIConversation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_decision_time = time.time()
        self.ai_decision_loop.start()
        self.timer_loop.start()
        logger.info("AutonomousAIConversation cog initialized")

    def cog_unload(self):
        self.ai_decision_loop.cancel()
        self.timer_loop.cancel()
        logger.info("AutonomousAIConversation cog unloaded")

    @tasks.loop(seconds=30)  # Check every 30 seconds
    async def ai_decision_loop(self):
        try:
            logger.info("AI decision loop started")
            sleep_duration = global_sleep
            logger.debug(f"Current sleep duration: {sleep_duration}")
            if sleep_duration > 0:
                logger.info(f"Sleeping for {sleep_duration} seconds")
                await asyncio.sleep(sleep_duration)
                self.last_decision_time = time.time()
                logger.info("Starting AI decision process")
                await self.ai_decision_process()
            else:
                logger.warning("Sleep duration is 0 or negative, skipping decision process")
        except Exception as e:
            logger.error(f"Error in ai_decision_loop: {e}")
            logger.error(traceback.format_exc())

    @tasks.loop(seconds=1)  # Run every second
    async def timer_loop(self):
        current_time = time.time()
        time_since_last_decision = current_time - self.last_decision_time
        time_until_next_decision = max(0, global_sleep - time_since_last_decision)
        logger.info(f"Time until next decision: {time_until_next_decision:.2f} seconds")

    async def ai_decision_process(self):
        try:
            # Choose a random environment
            environment = random.choice(["Development Environment", "Testing Environment"])
            logger.info(f"Selected environment: {environment}")
            
            # Get the last 50 messages from the chosen environment
            messages = read_last_50_messages(environment)
            
            if isinstance(messages, list) and messages and isinstance(messages[0], dict) and 'error' in messages[0]:
                logger.error(f"Error reading messages: {messages[0]['error']}")
                return

            logger.info("Starting AI conversation")

            # Always use Touka's character prompt
            character_name = "Touka"
            character_system_prompt = character_prompts["Touka"]

            # General system prompt
            system_prompt = f"""
            You are an AI assistant in a Discord bot, capable of engaging in conversations and making autonomous decisions. 
            Your persona is Touka Tsukioka. Embody this character in your responses and decision-making.

            {character_system_prompt}

            Your primary tasks are:
            1. Analyze recent messages in the chat environment.
            2. Decide whether to engage in the conversation based on the context.
            3. If engaging, formulate a response that adds value and stays in character as Touka.
            4. Determine an appropriate sleep duration before your next check.

            You have access to the following tools:
            - 'send_message': Use this to send a message to the chat if you decide to engage.

            Remember, quality of interaction is more important than quantity. Only engage when you can contribute meaningfully.
            """

            # Admin prompt for decision making
            admin_prompt = f"""
            Analyze the recent messages in the {environment} and decide whether to engage in conversation as Touka. 
            Here are your instructions:

            1. Read and understand the context of the recent messages.
            2. Decide if there's an opportunity for you to contribute meaningfully to the conversation.
            3. If you choose to engage, formulate a response that adds value to the discussion and stays in character as Touka.
            4. Determine an appropriate sleep duration before your next check (between 5 and 60 minutes).

            Recent messages:
            {messages}


            Based on this information, decide your next action. Your response should be in the following format:
            Decision: [Engage/Don't Engage]
            Reason: [Your reasoning]
            Action: [Your message if engaging, or 'None' if not]
            New Sleep Duration: [Duration in seconds]
            """

            # Call the AI conversation function with the system prompt and admin prompt
            ai_response = ai_conversation(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": admin_prompt}
                ],
                character_name=character_name,
                system_prompt=character_system_prompt,
                tools=tools
            )

            logger.info("AI conversation completed")

            # Parse the AI's decision
            decision_lines = ai_response.split('\n')
            decision = {}
            for line in decision_lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    decision[key.strip()] = value.strip()

            # Act on the AI's decision
            if decision.get('Decision') == 'Engage':
                await send_message(environment, decision.get('Action', ''))
                logger.info(f"Touka engaged in conversation in {environment}")
            else:
                logger.info(f"Touka chose not to engage in {environment}")

            # Set the new sleep duration
            new_sleep_duration = int(decision.get('New Sleep Duration', 300))  # Default to 5 minutes if parsing fails
            set_sleep(new_sleep_duration)
            logger.info(f"Next AI decision process in {new_sleep_duration} seconds")
        except Exception as e:
            logger.error(f"Error in ai_decision_process: {e}")
            logger.error(traceback.format_exc())

    @ai_decision_loop.before_loop
    async def before_ai_decision_loop(self):
        await self.bot.wait_until_ready()
        logger.info("AI decision loop is ready to start")

    @timer_loop.before_loop
    async def before_timer_loop(self):
        await self.bot.wait_until_ready()
        logger.info("Timer loop is ready to start")

def setup(bot):
    try:
        bot.add_cog(AutonomousAIConversation(bot))
        logger.info("AutonomousAIConversation cog added successfully")
    except Exception as e:
        logger.error(f"Error adding AutonomousAIConversation cog: {e}")
        logger.error(traceback.format_exc())