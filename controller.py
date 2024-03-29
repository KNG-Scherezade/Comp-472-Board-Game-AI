import model
import data
import view

import re

# process string input into components and check for issues 
def split_input_str(input_str):
    if input_str.count(".") < 2:
        data.set_error_message("Poor formatting - Not enough fields")
        return None, None, None, True
    input_arr = input_str.split(".")

    if input_arr[0] != "m" and input_arr[0] != "p":
        data.set_error_message("Poor formatting - misunderstood operation: " + input_arr[0])
        return None, None, None, True

    if input_arr[0] == "m":
        if len(re.findall("^[a-l]->[a-l]$", input_arr[1])) < 1:
            data.set_error_message("Poor formatting - Move interpreted wrong "
                                   "(" + input_arr[1] + ")")
            return None, None, None, True

        if len(re.findall("^([1-9]|[1][0-2])->([1-9]|[1][0-2])$", input_arr[2])) < 1:
            data.set_error_message("Poor formatting - Move interpreted wrong "
                                   "(" + input_arr[2] + ")")
            return None, None, None, True

    if input_arr[0] == "p":
        if len(re.findall("^[a-l]$", input_arr[1])) < 1:
            data.set_error_message("Poor formatting - Placement interpreted wrong "
                                   "(" + input_arr[1] + ")")
            return None, None, None, True

        if len(re.findall("^([1-9]|[1][0-2])$", input_arr[2])) < 1:
            data.set_error_message("Poor formatting - Placement interpreted wrong "
                                   "(" + input_arr[2] + ")")
            return None, None, None, True

    return input_arr[0], input_arr[1], input_arr[2], False

def convert_ta_input(input):
    input = input.lower()
    input_arr = input.split(" ")
    preffered_str = ""
    if len(input_arr) == 1:
        if len(re.findall("^[a-l]([1-9]|[1][0-2])$", input)) < 1:
            data.set_error_message("Poor formatting")
            return "",True
        preffered_str = "p." + input_arr[0][0:1] + "." + input_arr[0][1:]
    elif len(input_arr) == 2:
        if len(re.findall("^[a-l]([1-9]|[1][0-2]) [a-l]([1-9]|[1][0-2])$", input)) < 1:
            data.set_error_message("Poor formatting")
            return "",True
        preffered_str = "m." + input_arr[0][0:1] +"->" + input_arr[1][0:1] + "." + input_arr[0][1:]  +"->" + input_arr[1][1:] 
    else:
        data.set_error_message("Poor formatting")
        return "",True
    return preffered_str, False

# game loop to be done by a human
def game_loop(input_str_orig, ai_trial_input=False):
    if input_str_orig == "RESIGN":
        if not ai_trial_input:
            view.print_resign()
        return False
    input_str, error = convert_ta_input(input_str_orig)
    if error:
        if not ai_trial_input:
            view.print_error()
        return True
    operation, x_position, y_position, error = split_input_str(input_str)
    if error:
        if not ai_trial_input:
            view.print_error()
        return True

    if operation == "m":
        error = model.check_losing_move(operation, x_position, y_position)
    elif operation == "p":
        error = model.check_token_count()
    if error:
        if not ai_trial_input:
            view.print_error()
        return True

    error = model.check_overlap(operation, x_position, y_position)
    if error:
        if not ai_trial_input:
            view.print_error()
        return True

    model.place_piece_on_board(operation, x_position, y_position)
    if not ai_trial_input:
        view.print_board()
        view.print_last_move(input_str_orig)

    win_check = model.check_win(operation, x_position, y_position)
    if win_check:
        if not ai_trial_input:
            view.print_winner()
        return False

    model.increment_counters(operation)
    draw_check = model.check_draw()
    if draw_check:
        if not ai_trial_input:
            view.print_draw()
        return False
    model.swap_turn()
    data.set_error_message("unset")
    return True
