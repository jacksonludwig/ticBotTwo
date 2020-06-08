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


@client.command(aliases=['c'])
async def clear(context):
    game_board = Board()
    await context.send(game_board.format_board())


@client.command(aliases=['p'])
async def play(context, symbol, position):
    symbol, position = game_board.normalize_inputs(symbol, position)
    game_board.take_move(symbol, position)
    await context.send(game_board.format_board())


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
