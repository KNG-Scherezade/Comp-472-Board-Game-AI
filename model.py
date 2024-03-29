import data


def check_move_count():
    if data.get_both_move_count() == 30:
        data.set_error_message("All moves done")
        return True
    return False


# check if a move will result in player losing
def check_losing_move(operation, x_position, y_position):
    # loss only occurs when you didn't place last
    if data.get_last_placement_ascii() == data.get_active_player_ascii():
        return False

    if operation == "m":
        x_position = ord(x_position.split("->")[0]) - 97
        y_position = 10 - int(y_position.split("->")[0])
        fail = False
    if check_x_from_center(x_position - 1, y_position):
        fail = True
    if check_x_from_center(x_position + 1, y_position):
        fail = True
    if check_x_from_center(x_position, y_position - 1):
        fail = True
    if check_x_from_center(x_position, y_position + 1):
        fail = True
    if fail:
        data.set_error_message("This move will result in a loss")
    return fail


def check_token_count():
    if data.get_active_placement_count() == data.get_max_tokens():
        data.set_error_message("All tokens used up")
        return True
    return False


def check_overlap(operation, x_position, y_position):
    board = data.get_board()
    if operation == "m":
        x_position_new = ord(x_position.split("->")[1]) - 97
        y_position_new = 10 - int(y_position.split("->")[1])

        x_position_rm = ord(x_position.split("->")[0]) - 97
        y_position_rm = 10 - int(y_position.split("->")[0])
        if board[y_position_rm, x_position_rm] != data.get_active_player_ascii():
            data.set_error_message("No piece to move")
            return True
    elif operation == "p":
        x_position_new = ord(x_position) - 97
        y_position_new = 10 - int(y_position)

    if board[y_position_new, x_position_new] != data.get_empty_ascii():
        data.set_error_message("Space Occupied")
        return True
    return False


def place_piece_on_board(operation, x_position, y_position):
    board = data.get_board()
    if operation == "m":
        x_position_new = ord(x_position.split("->")[1]) - 97
        y_position_new = 10 - int(y_position.split("->")[1])

        x_position_rm = ord(x_position.split("->")[0]) - 97
        y_position_rm = 10 - int(y_position.split("->")[0])
        board[y_position_rm, x_position_rm] = data.get_empty_ascii()
    elif operation == "p":
        x_position_new = ord(x_position) - 97
        y_position_new = 10 - int(y_position)
        data.set_last_placement_ascii(data.get_active_player_ascii())
    board[y_position_new, x_position_new] = data.get_active_player_ascii()


# evaluates if an x is on a certain position
def check_x_from_center(x, y, reverse_ascii=False):
    board = data.get_board()
    # proceed by checking invalidating conditions
    if reverse_ascii:
        data.reverse_player_data()
    if not (x >= 0 and y < 10 and x < 12 and y >= 0 and board[y, x] == data.get_active_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()
        return False
    if not (x - 1 >= 0 and y + 1 < 10 and board[y + 1, x - 1] == data.get_active_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()    
        return False
    if not (x + 1 < 12 and y + 1 < 10 and board[y + 1, x + 1] == data.get_active_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()        
        return False
    if not (x - 1 >= 0 and y - 1 >= 0 and board[y - 1, x - 1] == data.get_active_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()
        return False
    if not (x + 1 < 12 and y - 1 >= 0 and board[y - 1, x + 1] == data.get_active_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()
        return False

    # check cross X
    if (x - 1 > 0 and x + 1 <= 12 and board[y, x + 1] == data.get_opposing_player_ascii() and
            board[y, x - 1] == data.get_opposing_player_ascii()) or \
            (y - 1 > 0 and y + 1 <= 10 and board[y + 1, x] == data.get_opposing_player_ascii() and
             board[y - 1, x] == data.get_opposing_player_ascii()):
        if reverse_ascii:
            data.reverse_player_data()
        return False
    if reverse_ascii:
        data.reverse_player_data()
    return True


# check if player wins
def check_win(operation, x_position, y_position):
    if operation == "m":
        x_position = ord(x_position.split("->")[1]) - 97
        y_position = 10 - int(y_position.split("->")[1])
    elif operation == "p":
        x_position = ord(x_position) - 97
        y_position = 10 - int(y_position)
    data.win_state = "winner"
    data.set_error_message("unset")
    if check_x_from_center(x_position, y_position):
        return True
    if check_x_from_center(x_position - 1, y_position + 1):
        return True
    if check_x_from_center(x_position + 1, y_position + 1):
        return True
    if check_x_from_center(x_position - 1, y_position - 1):
        return True
    if check_x_from_center(x_position + 1, y_position - 1):
        return True
    data.win_state = "unset"
    return False


def increment_counters(operation):
    if operation == "m":
        data.increment_active_move_count()
    elif operation == "p":
        data.increment_active_placement_count()
    else:
        print("lol what")


def check_draw():
    return data.get_both_movement_count() >= data.get_max_combo_moves()


def swap_turn():
    data.reverse_player_data()
