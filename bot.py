import discord
from discord.ext import commands
from board import Board

import logging
import json_reader
import board_connector

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
    symbol = symbol.upper()
    if not board_connector.is_position_okay(position):
        await context.send(board_connector.make_pos_error())
    elif not board_connector.is_symbol_okay(symbol):
        await context.send(board_connector.make_sym_error())
    else:
        position = int(position) - 1
        if not game_board.is_spot_taken(position):
            await context.send(board_connector.make_availablity_error())
        else:
            game_board.take_move(symbol, position)
            await context.send(game_board.format_board())
            if game_board.is_win(symbol):
                await context.send(board_connector.win_print(symbol))
            elif game_board.is_tie():
                await context.send(board_connector.tie_print())


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
