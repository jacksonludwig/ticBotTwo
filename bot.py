import discord
from discord.ext import commands
from board import Board

import logging
import json_reader
import board_connector

client = commands.Bot(command_prefix="%")
TOKEN = json_reader.get_token()

game_board = Board()

errors = [board_connector.check_for_sym_error,
          board_connector.check_for_pos_error,
          board_connector.check_for_range_error,
          board_connector.check_for_avail_error]


@client.event
async def on_ready():
    logging.info("bot running")


@client.command(aliases=['c'])
async def clear(context):
    global game_board
    game_board = Board()
    await context.send(game_board.format_board())


@client.command(aliases=['p'])
async def play(context, symbol, position):
    symbol = symbol.upper()

    if await board_connector.check_errors(errors, context, game_board,
                                          symbol, position):
        return

    game_board.take_move(symbol, position)
    await board_connector.send_board(context, game_board)
    await board_connector.check_win_or_tie(context, game_board, symbol)


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
