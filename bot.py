import discord
from discord.ext import commands

import logging
import json_reader

client = commands.Bot(command_prefix="%")
TOKEN = json_reader.get_token()


@client.event
async def on_ready():
    logging.info("bot running")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
