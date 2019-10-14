import numpy
import model
import view

current_turn = 'r'


def split_input_str(input_str):
    input_arr = input_str.split(".")
    return input_arr[0], input_arr[1], input_arr[2]


def swap_turn():
    global current_turn
    current_turn = current_turn = 'w' if current_turn == 'r' else current_turn = 'r'


def run_human_routine(input_str):
    if input_str == "RESIGN":
        view.print_resign(current_turn)
        return False

    operation, x_position, y_position = controller.split_input_str(input_str)

    if operation == "m":
        error = model.check_move_count(current_turn)
        if error:
            view.print_error()
        error = model.check_losing_move(x_position, y_position)
    elif operation == "p":
        error = model.check_token_count(current_turn)
        return True
    if error:
        view.print_error()
        return True

    error = model.check_overlap(operation, x_position, y_position)
    if error:
        view.print_error()
        return True

    model.place_piece_on_board(current_turn, operation, x_position, y_position)

    win_check = model.check_win(current_turn, operation, x_position, y_position)
    if win_check:
        view.print_winner(current_turn)
        return False

    model.increment_counters(current_turn, operation)

    draw_check = model.check_draw(current_turn)
    if draw_check:
        view.print_draw()
        return False

    view.print_board()
    view.print_last_move(current_turn, operation, x_position, y_position)
    controller.swap_turn()
    return True
