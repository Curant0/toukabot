import discord
from discord.ext import commands
from discord_package import util


class AICommands(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @discord.slash_command()
    @util.is_channel_whitelisted()
    async def some_command(self):
        pass
        



