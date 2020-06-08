import discord
from discord.ext import commands

import logging

client = commands.Bot(command_prefix="&")


@client.event
async def on_ready():
    logging.info("bot running")
