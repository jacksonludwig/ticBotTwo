import discord
from discord.ext import commands

import logging
import json_reader
from board import Board

client = commands.Bot(command_prefix="%")
TOKEN = json_reader.get_token()

game_board = Board()


@client.event
async def on_ready():
    logging.info("bot running")


@client.command()
async def clear(context):
    game_board = Board()
    await context.send(game_board.format_board())


@client.command(aliases=["play", 'p'])
async def take_turn(context):
    # TODO take turn
    await context.send("take turn")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
