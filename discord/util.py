from discord import ApplicationContext
from os import getenv
WHITELISTED_CHANNELS = getenv('DEV_CHANNEL_ID'), getenv('TEST_CHANNEL_ID')

def is_channel_whitelisted(ctx: ApplicationContext) -> bool:
    if str(ctx.channel_id) not in WHITELISTED_CHANNELS:
        return False
    return True

