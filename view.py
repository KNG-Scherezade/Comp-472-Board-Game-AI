import data


def print_resign():
    print("\t" + data.get_active_player_symbol() + " has resigned from the match.\n"
                                                   "\t\033[1m" + data.get_opposing_player_symbol() + " Wins\033[0m")


def print_error():
    print("\t\033[1mIssue: " + data.get_error_message() + "\033[0m")


def print_winner():
    print("\t\033[1mWinner: " + chr(data.get_active_player_ascii()) + "\033[0m")


def print_draw():
    print("\t\033[1mDraw: All moves and tokens exhausted\033[0m")


def print_board():
    board_str = ""
    i = 10
    for row in data.get_board():
        board_str += "\033[1m" + str(i) + "\033[0m\t"
        i = i - 1
        for entry in row:
            if entry == 119:
                board_str += "\033[100m" + (chr(119) + "\033[0m ")
            elif entry == 114:
                board_str += "\033[41m" + (chr(114) + "\033[0m ")
            else:
                board_str += "\033[107m" + (chr(data.get_empty_ascii()) + "\033[0m ")
        board_str += "\033[0m\n"
    board_str += "\t\033[1ma b c d e f g h i j k l\033[0m"
    print(board_str)


def print_last_move(operation, x_position, y_position):
    if operation == 'm':
        print("\33[3m" + chr(data.get_active_player_ascii()) +
              " moved with " + x_position + "," + y_position + "\33[0m")
    if operation == 'p':
        print("\33[3m" + chr(data.get_active_player_ascii()) +
              " placed at " + x_position + "," + y_position +
              "(" + str(data.get_active_placement_count() + 1) + "/" + str(data.get_max_tokens()) + ")\33[0m")
