import numpy
import model
import view

current_turn = 'r'


def run_human_routine(input_str):
    if input_str == "RESIGN":
        view.print_resign(current_turn)
        return False
    input_arr = input_str.split(".")
    operation = input_arr[0]
    x_position = input_arr[1]
    y_position = input_arr[2]

    if operation == "m":
        error = model.check_move_count(current_turn)
        if error:
            view.printErr()
        error = model.check_losing_move(x_position, y_position)
    elif operation == "p":
        error = model.check_token_count(current_turn)
    if error:
        view.printErr()

    error = model.check_overlap(operation, x_position, y_position)
    if error:
        view.printErr()


    return True
