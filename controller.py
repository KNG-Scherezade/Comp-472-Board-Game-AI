import model
import data
import view

import re


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


def run_human_routine(input_str):
    if input_str == "RESIGN":
        view.print_resign()
        return False

    operation, x_position, y_position, error = split_input_str(input_str)
    if error:
        view.print_error()
        return True

    if operation == "m":
        error = model.check_losing_move(operation, x_position, y_position)  # TODO
    elif operation == "p":
        error = model.check_token_count()
    if error:
        view.print_error()
        return True

    error = model.check_overlap(operation, x_position, y_position)
    if error:
        view.print_error()
        return True

    model.place_piece_on_board(operation, x_position, y_position)
    view.print_board()
    view.print_last_move(operation, x_position, y_position)

    win_check = model.check_win(operation, x_position, y_position)  # TODO
    if win_check:
        view.print_winner()
        return False

    model.increment_counters(operation)
    draw_check = model.check_draw()
    if draw_check:
        view.print_draw()
        return False

    model.swap_turn()
    return True
