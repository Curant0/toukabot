import discord
from discord.ext import commands
from util import is_channel_whitelisted
import logging
from logging_setup import configure_logger
aic_logger = configure_logger('AI_COG', logging.DEBUG)


class AICommands(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @discord.slash_command()
    @is_channel_whitelisted()
    async def interact(self, ctx: discord.ApplicationContext, query: str):
        # TODO: Database: Read some user data, balance and config (ephemeral, girl)
        # if there's no user, create a new one.
        # Consider defaults, 1, False and Touka
        balance: int
        ephemeral: bool
        girl: str  # appeared as character_name in main2.
        balance, ephemeral, girl = some_bullshit()

        aic_logger.debug(f'User {ctx.author.name} entered the query: {query}')
        channel_id = ctx.channel_id
        channel = ctx.channel.name
        aic_logger.debug(f'In channel: {channel} ({channel_id})')
        
        if balance <= 0:
            await ctx.send_response(embed=EMPTY_CASH, ephemeral=ephemeral)
            return

        # TODO: Find how many tokens were used
            
        # TODO: Get some @tool that gets channel data
        


