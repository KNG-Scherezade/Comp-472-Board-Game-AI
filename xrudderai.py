
import statespacedepth3
import statespacegenerator

import data 
import model 
import controller 
import numpy as np
import queue
import math
import time



precomputed_depth = 2
depth = 0

def interpret_move(numeric_move):
    print(numeric_move)
    numeric_move = str(numeric_move).split("9")
    string_move = ""
    if numeric_move[0] == "1":
        string_move = "p." + chr(int(format(int(numeric_move[1], 8) + 96, 'd'))) + "." + str(format(int(numeric_move[2], 8), 'd'))
    else:
        string_move = "m." + str(chr(format(int(numeric_move[1], 8) + 96, 'd'))) + "->" + str(chr(format(int(numeric_move[2], 8) + 96, 'd'))) + "." \
            + str(format(int(numeric_move[1], 8), 'd')) + "->" + str(format(int(numeric_move[2], 8), 'd'))
    return string_move
    
def evaluate_heuristic(board):
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    h = 0
    for x in range(0,12):
        for y in range(0,10):
            if board[y][x] == active_ascii:
                if model.check_x_from_center(x, y):
                    h+=200
                
                if x - 1 >= 0 and y + 1 < 10:
                    if board[y + 1][x - 1] == opposing_ascii:
                        h -= 1
                    elif board[y + 1][x - 1] == active_ascii:
                        h += 2
                        
                if x - 1 >= 0:
                    if board[y][x - 1] == opposing_ascii:
                        h -= 2
                    elif board[y][x - 1] == active_ascii:
                        h += 1
                        
                if y + 1 < 10:
                    if board[y + 1][x] == opposing_ascii:
                        h -= 2
                    elif board[y + 1][x] == active_ascii:
                        h += 1
                        
                if x - 1 >= 0 and y - 1 >= 0:
                    if board[y - 1][x - 1] == opposing_ascii:
                        h -= 1
                    elif board[y - 1][x - 1] == active_ascii:
                        h += 2
                        
                if y - 1 >= 0:
                    if board[y - 1][x] == opposing_ascii:
                        h -= 2
                    elif board[y - 1][x] == active_ascii:
                        h += 1
                        
                if x + 1 < 12 and y + 1 < 10:
                    if board[y + 1][x + 1] == opposing_ascii:
                        h -= 1
                    elif board[y + 1][x + 1] == active_ascii:
                        h += 2
                        
                if x + 1 < 12:
                    if board[y][x + 1] == opposing_ascii:
                        h -= 2
                    elif board[y][x + 1] == active_ascii:
                        h += 1
                        
                if x + 1 < 12 and y - 1 < 10:
                    if board[y - 1][x + 1] == opposing_ascii:
                        h -= 1
                    elif board[y - 1][x + 1] == active_ascii:
                        h += 2
    return h

def d2_find_best_solution_no_store(min):
    global depth
    max = not min
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"
    current_best_heuristic = 0

    store_board_d0 = np.copy(data.board)
    store_player_data_d0 = np.copy(data.get_raw_player_data())
    store_win_state_d0 = data.win_state
    store_last_placement_ascii_d0 = data.last_placement_ascii

    for xd1 in "abcdefghijkl":
        for yd1 in range(1,11):
            # placement
            controller.game_loop("p." + str(xd1) + '.' + str(yd1), True)
            if data.get_error_message() == "unset":
                if data.win_state != "unset":
                    print("ws")
                    return "p." + str(xd1) + '.' + str(yd1)
                store_board_d1 = np.copy(data.board)
                store_player_data_d1 = np.copy(data.get_raw_player_data())
                store_win_state_d1 = data.win_state
                store_last_placement_ascii_d1 = data.last_placement_ascii
                inner_break = False
                
                for xd2 in "abcdefghijkl":
                    for yd2 in range(1,11):
                        controller.game_loop("p." + str(xd2) + '.' + str(yd2), True)
                        if data.get_error_message() == "unset":
                            h = evaluate_heuristic(data.board)
                            if max and h < beta or min and h > alpha:
                                inner_break = True
                                break
                            if not min and h >= current_best_heuristic or not max and h <= current_best_heuristic:
                                current_best_move = "p." + str(xd1) + '.' + str(yd1)
                                current_best_heuristic = h 
                            
                            data.board = np.copy(store_board_d1)
                            data.player_data = np.copy(store_player_data_d1)
                            data.win_state = store_win_state_d1
                            data.last_placement_ascii = store_last_placement_ascii_d1
                        for xdm2 in "abcdefghijkl":
                            for ydm2 in range(1,11):
                                if data.board[ydm2 - 1][ord(xdm2) - 97] != data.empty_ascii:
                                    controller.game_loop("m." + str(xd2) + '->' + 
                                        str(xdm2) + '.' + str(yd2) + '->' +  str(ydm2), True)
                                    if data.get_error_message() == "unset":
                                        h = evaluate_heuristic(data.board)
                                        if max and h < beta or min and h > alpha:
                                            inner_break = True
                                            break
                                        if not min and h >= current_best_heuristic or not max and h <= current_best_heuristic:
                                            current_best_move = "p." + str(xd1) + '.' + str(yd1)
                                            current_best_heuristic = h 
                                        
                                        data.board = np.copy(store_board_d1)
                                        data.player_data = np.copy(store_player_data_d1)
                                        data.win_state = store_win_state_d1
                                        data.last_placement_ascii = store_last_placement_ascii_d1    
                            if inner_break:
                                break
                        data.error_msg = "unset"
                    if inner_break:
                        break
            if not min and current_best_heuristic >= beta:
                beta = current_best_heuristic  
            elif not max and current_best_heuristic <= alpha:
                alpha = current_best_heuristic
            current_best_heuristic = 0
            data.board = np.copy(store_board_d0)
            data.player_data = np.copy(store_player_data_d0)
            data.win_state = store_win_state_d0
            data.last_placement_ascii = store_last_placement_ascii_d0
            data.error_msg = "unset"  
            
            # movement
            for xdm1 in "abcdefghijkl":
                for ydm1 in range(1,11):
                    if data.board[ydm1 - 1][ord(xdm1) - 97] != data.empty_ascii:
                        controller.game_loop("m." + str(xd1) + '->' + str(xdm1) + '.' + str(yd1) + '->' +  str(ydm1), True)
                        if data.get_error_message() == "unset":
                            if data.win_state != "unset":
                                return "m." + str(xd1) + '->' + str(xdm1) + '.' + str(yd1) + '->' +  str(ydm1)
                            store_board_d1 = np.copy(data.board)
                            store_player_data_d1 = np.copy(data.get_raw_player_data())
                            store_win_state_d1 = data.win_state
                            store_last_placement_ascii_d1 = data.last_placement_ascii
                            inner_break = False
                            
                            for xd2 in "abcdefghijkl":
                                for yd2 in range(1,11):
                                    controller.game_loop("p." + str(xd2) + '.' + str(yd2), True)
                                    if data.get_error_message() == "unset":
                                        h = evaluate_heuristic(data.board)
                                        if max and h < beta or min and h > alpha:
                                            inner_break = True
                                            break
                                        if not min and h >= current_best_heuristic or not max and h <= current_best_heuristic:
                                            current_best_move = "p." + str(xd1) + '.' + str(yd1)
                                            current_best_heuristic = h 
                                        
                                        data.board = np.copy(store_board_d1)
                                        data.player_data = np.copy(store_player_data_d1)
                                        data.win_state = store_win_state_d1
                                        data.last_placement_ascii = store_last_placement_ascii_d1
                                    for xdm2 in "abcdefghijkl":
                                        for ydm2 in range(1,11):
                                            if data.board[ydm2 - 1][ord(xdm2) - 97] != data.empty_ascii:
                                                controller.game_loop("m." + str(xd2) + '->' + 
                                                    str(xdm2) + '.' + str(yd2) + '->' +  str(ydm2), True)
                                                if data.get_error_message() == "unset":
                                                    h = evaluate_heuristic(data.board)
                                                    if max and h < beta or min and h > alpha:
                                                        inner_break = True
                                                        break
                                                    if not min and h >= current_best_heuristic or not max and h <= current_best_heuristic:
                                                        current_best_move = "p." + str(xd1) + '.' + str(yd1)
                                                        current_best_heuristic = h 
                                                    
                                                    data.board = np.copy(store_board_d1)
                                                    data.player_data = np.copy(store_player_data_d1)
                                                    data.win_state = store_win_state_d1
                                                    data.last_placement_ascii = store_last_placement_ascii_d1    
                                        if inner_break:
                                            break
                                    data.error_msg = "unset"
                                if inner_break:
                                    break        
                                    
                            if not max and current_best_heuristic <= alpha:
                                alpha = current_best_heuristic  
                            elif not min and current_best_heuristic >= beta:
                                beta = current_best_heuristic
                        if not min and current_best_heuristic >= beta:
                            beta = current_best_heuristic  
                        elif not max and current_best_heuristic <= alpha:
                            alpha = current_best_heuristic
                        current_best_heuristic = 0
                        data.board = np.copy(store_board_d0)
                        data.player_data = np.copy(store_player_data_d0)
                        data.win_state = store_win_state_d0
                        data.last_placement_ascii = store_last_placement_ascii_d0
                        data.error_msg = "unset"  
    data.error_msg = "unset"  
    data.board = np.copy(store_board_d0)
    data.player_data = np.copy(store_player_data_d0)
    data.win_state = store_win_state_d0
    data.last_placement_ascii = store_last_placement_ascii_d0        
    print(current_best_move)
    return current_best_move


    
if __name__ == "__main__":
    start = time.time()
    print(d2_find_best_solution_no_store(False))

    end = time.time()
    print(end - start)