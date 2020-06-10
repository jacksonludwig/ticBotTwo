import discord
from discord.ext import commands


async def make_pos_error(context):
    await context.send("```Position must be 1-9.```")


async def make_sym_error(context):
    await context.send("```Symbol must be \"X\" or \"O\" only.```")


async def make_availablity_error(context):
    await context.send("```Position must correspond to an open cell.```")


def is_position_okay(position):
    return len(position) == True and position.isdigit()


def is_pos_range_okay(position):
    return position >= 0 and position < 10


def is_symbol_okay(symbol):
    return symbol == "X" or symbol == "O"


async def win_print(context, symbol):
    await context.send(f"```{symbol} wins```")


async def tie_print(context):
    await context.send("```Game tied```")


async def check_for_pos_error(context, board, symbol, position):
    if not is_position_okay(position):
        await make_pos_error(context)
        return True
    return False


async def check_for_sym_error(context, board, symbol, position):
    if not is_symbol_okay(symbol):
        await make_sym_error(context)
        return True
    return False


async def check_for_range_error(context, board, symbol, position):
    position = int(position) - 1
    if not is_pos_range_okay(position):
        await make_pos_error(context)
        return True
    return False


async def check_for_avail_error(context, board, symbol, position):
    position = int(position) - 1
    if not board.is_spot_open(position):
        await make_availablity_error(context)
        return True
    return False


async def check_win_or_tie(context, board, symbol):
    if board.is_win(symbol):
        await win_print(context, symbol)
    elif board.is_tie():
        await tie_print(context)


async def check_errors(error_list, context, game_board, symbol, position):
    for check in error_list:
        if await check(context, game_board, symbol, position):
            return True
    return False


async def send_board(context, board):
    await context.send(board.format_board())
