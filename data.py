import numpy as np

# numpy array where index 0 is white and index 1 is red
# index [n][0] is color
# index [n][1] is moved pieces
# index [n][2] is placed pieces

p1_ascii = 119
p2_ascii = 114
player_data = np.array([[p1_ascii, 0, 0], [p2_ascii, 0, 0]])

board = np.empty((10, 12), np.int8)
empty_ascii = 48
board.fill(empty_ascii)

error_msg = "unset"

win_state = "unset"

last_placement_ascii = 0

max_tokens = 15

max_moves = 30

def get_max_tokens():
    return max_tokens


def get_max_combo_moves():
    return max_moves


def get_board():
    return board

def get_last_placement_ascii():
    return last_placement_ascii


def get_win_state():
    return win_state


def get_error_message():
    return error_msg


def get_raw_player_data():
    return player_data


def reverse_player_data():
    global player_data
    player_data = np.flip(player_data, 0)


def get_active_move_count():
    return player_data[0, 1]


def get_both_movement_count():
    return player_data[0, 1] + player_data[1, 1]


def get_active_placement_count():
    return player_data[0, 2]


def get_both_placement_count():
    return player_data[0, 2] + player_data[1, 2]


def get_active_player_ascii():
    return player_data[0, 0]


def get_opposing_player_ascii():
    return player_data[1, 0]


def get_empty_ascii():
    return empty_ascii


def increment_active_move_count():
    player_data[0, 1] = player_data[0, 1] + 1


def increment_active_placement_count():
    player_data[0, 2] = player_data[0, 2] + 1


def decrement_active_move_count():
    player_data[0, 1] = player_data[0, 1] - 1


def decrement_active_placement_count():
    player_data[0, 2] = player_data[0, 2] - 1

def set_last_placement_ascii(symbol):
    global last_placement_ascii
    last_placement_ascii = symbol


def set_win_state(state):
    return win_state


def set_error_message(msg):
    global error_msg
    error_msg = msg


def set_raw_player_data(data_arr):
    global player_data
    player_data = data_arr


def set_board(new_board):
    global board
    board = new_board