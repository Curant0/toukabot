from discord.ext import commands
from os import getenv
# TODO: Try to make a easier launch
WHITELISTED_CHANNELS = [getenv('DEV_CHANNEL_ID'), getenv('TEST_CHANNEL_ID')]

# Changed function to a decorator
def is_channel_whitelisted():
    async def predicate(ctx):
        return ctx.channel.id in WHITELISTED_CHANNELS
    return commands.check(predicate)


# TODO: Make an embed out of this
support_message = (
    "Looking to power up? Your support accelerates our journey into the future of AI. "
    "Top up your token balance and keep the code compiling by buying me a coffee! "
    "For each dollar, you'll receive an equal amount in tokens to continue interacting with the bot. "
    "Click here to support and energize our progress: https://www.buymeacoffee.com/womp_womp_ "
    "Your contribution is the caffeine in our coding coffee. Thank you for brewing success with us!"
)


# TODO: Database balance interaction, move to the ORM.
async def process_command(interaction, query):
    user_id = interaction.user.id
    balance = get_balance(user_id)
    if balance is None:
        add_new_user(user_id)
        balance = 1.0000 # Initial balance

    # Your logic to process the command and generate a response
    response, tokens_used = your_response_generation_function(query)
    
    cost = calculate_cost(tokens_used)
    update_balance(user_id, cost)
    log_transaction(user_id, tokens_used, cost)  # Optional
    
    new_balance = balance - cost
    response += f"\nThis interaction costed ${cost:.4f}. Your new balance is ${new_balance:.2f}."
    
    await interaction.response.send_message(response, ephemeral=True)


