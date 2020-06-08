def make_pos_error():
    return "```Position must be 1-9.```"


def make_sym_error():
    return "```Symbol must be \"X\" or \"O\" only.```"


def make_availablity_error():
    return "```Position must correspond to an open cell.```"


def is_position_okay(position):
    return len(position) == 1 and position.isdigit()


def is_symbol_okay(symbol):
    return symbol == "X" or symbol == "O"


def win_print(symbol):
    return f"```{symbol} wins```"


def tie_print():
    return "```Game tied```"
