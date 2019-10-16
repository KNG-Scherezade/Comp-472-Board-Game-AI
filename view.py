import data


def print_resign():
    print("\t" + chr(data.get_active_player_ascii()) + " has resigned from the match.\n"
                                                   "\t" + chr(data.get_opposing_player_ascii()) + " Wins")


def print_error():
    print("\tIssue: " + data.get_error_message() + "")


def print_winner():
    print("\t\033[1mWinner: " + chr(data.get_active_player_ascii()) + "")


def print_draw():
    print("\tDraw: All moves and tokens exhausted")


# use terminal colors to decorate the board in the terminal
def print_board():
    board_str = ""
    i = 10
    for row in data.get_board():
        board_str += "" + str(i) + "\t"
        i = i - 1
        for entry in row:
            if entry == 119:
                board_str += "" + (chr(119) + " ")
            elif entry == 114:
                board_str += "" + (chr(114) + " ")
            else:
                board_str += "" + (chr(data.get_empty_ascii()) + " ")
        board_str += "\n"
    board_str += "\ta b c d e f g h i j k l"
    print(board_str)


def print_last_move(operation, x_position, y_position):
    if operation == 'm':
        print("" + chr(data.get_active_player_ascii()) +
              " moved with " + x_position + "," + y_position + "")
    if operation == 'p':
        print("" + chr(data.get_active_player_ascii()) +
              " placed at " + x_position + "," + y_position +
              "(" + str(data.get_active_placement_count() + 1) + "/" + str(data.get_max_tokens()) + ")")
