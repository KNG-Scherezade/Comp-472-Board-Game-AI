
import data 
import model 
import controller 
import numpy as np
import queue
import math
import time

move_heuristic = 0
defence_weight = 1
positional_weight = 0.5
time_cutoff = True
max_time = 4.99
start = 0
def positional_convolution(board, y, x):
    h = 0
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    if board[y][x] == active_ascii:
        h += (-abs(y - 4.5) + 4.5) / 4.5
        h += (-abs(x - 5.5) + 5.5) / 5.5
    elif board[y][x] == opposing_ascii:
        h -= (-abs(y - 4.5) + 4.5) / 4.5
        h -= (-abs(x - 5.5) + 5.5) / 5.5
    return h * positional_weight

def twoway_convolution(board, y, x):
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    h = 0
    if y + 2 >= 10 or x + 2 >= 12:
        return h
    board = board[y:y+2, x:x+2]

    if board[0,0] == active_ascii:
        if board[0,1] == active_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1       
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1 
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1            
    elif board[0,0] == opposing_ascii:
        if board[0,1] == active_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1       
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1 
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1 
    else:
        if board[0,1] == active_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1       
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1 
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 1
                else:
                    h += 1
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += -1
                else:
                    h += -1          
            else:
                if board[1,1] == active_ascii:
                    h += 1
                elif board[1,1] == opposing_ascii:
                    h += 0
                else:
                    h += 1         
    return h

def threeway_convolution(board, y, x):
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    h = 0
    if y + 3 >= 10 or x + 3 >= 12:
        return h
    board = board[y:y+3, x:x+3]
    
    if board[0,0] == active_ascii and board[1,1] == active_ascii and board[2,2] == active_ascii \
        and board[2,0] == active_ascii and board[0,2] == active_ascii and not(board[0,1] == opposing_ascii and board[2,1] == opposing_ascii \
        or board[1,0] == opposing_ascii and board[1,2] == opposing_ascii):
        h = float("-inf")
    elif board[0,0] == opposing_ascii and board[1,1] == opposing_ascii and board[2,2] == opposing_ascii \
        and board[2,0] == opposing_ascii and board[0,2] == opposing_ascii and not(board[0,1] == active_ascii and board[2,1] == active_ascii \
        or board[1,0] == active_ascii and board[1,2] == active_ascii):
        h = float("inf")
    elif not(board[0,1] == opposing_ascii or board[2,1] == opposing_ascii or board[1,0] == opposing_ascii or board[1,2] == opposing_ascii):
        if (board[0,0] == active_ascii and board[1,1] == active_ascii and board[0,2] == active_ascii) or \
            (board[0,0] == active_ascii and board[1,1] == active_ascii and board[2,0] == active_ascii) or \
            (board[2,0] == active_ascii and board[1,1] == active_ascii and board[2,2] == active_ascii) or \
            (board[2,2] == active_ascii and board[1,1] == active_ascii and board[0,2] == active_ascii):
            h += 10
    elif not(board[0,1] == active_ascii or board[2,1] == active_ascii or board[1,0] == active_ascii or board[1,2] == active_ascii):
        if (board[0,0] == opposing_ascii and board[1,1] == opposing_ascii and board[0,2] == opposing_ascii) or \
            (board[0,0] == opposing_ascii and board[1,1] == opposing_ascii and board[2,0] == opposing_ascii) or \
            (board[2,0] == opposing_ascii and board[1,1] == opposing_ascii and board[2,2] == opposing_ascii) or \
            (board[2,2] == opposing_ascii and board[1,1] == opposing_ascii and board[0,2] == opposing_ascii):
            h += -10
    
    return h

def evaluate_heuristic(board):
    global start
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    h = 0
    for x in range(0,12):
        if time_cutoff and time.time() - start > max_time:
            break
        for y in range(0,10):
            if time_cutoff and time.time() - start > max_time:
                break
            if data.board[y, x] != data.empty_ascii:
                h += twoway_convolution(board, y, x)
                h += threeway_convolution(board, y, x)
                h += positional_convolution(board, y, x) * 15 / data.get_both_placement_count()
    return h
     

def d2_find_best_solution_no_store():
    global start
    start = time.time()  
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"

    store_board_d0 = np.copy(data.board)
    store_player_data_d0 = np.copy(data.get_raw_player_data())
    store_win_state_d0 = data.win_state
    store_last_placement_ascii_d0 = data.last_placement_ascii
    resign_case_move = ""
    for xd1 in "abcdefghijkl":
        if time_cutoff and time.time() - start > max_time:
            break
        for yd1 in range(1,11):
            if time_cutoff and time.time() - start > max_time:
                break
            # placement
            if data.get_active_placement_count() < data.max_tokens:
                exit_reached = not controller.game_loop(str(xd1) + str(yd1), True)
                if data.get_error_message() == "unset":
                    resign_case_move = str(xd1) + str(yd1)
                    if data.win_state != "unset":
                        exit_reached = True
                    if exit_reached:
                        data.error_msg = "unset"  
                        data.board = np.copy(store_board_d0)
                        data.player_data = np.copy(store_player_data_d0)
                        data.win_state = store_win_state_d0
                        data.last_placement_ascii = store_last_placement_ascii_d0     
                        print("exit")
                        print(str(xd1) + str(yd1))
                        return str(xd1) + str(yd1)
                    store_board_d1 = np.copy(data.board)
                    store_player_data_d1 = np.copy(data.get_raw_player_data())
                    store_win_state_d1 = data.win_state
                    store_last_placement_ascii_d1 = data.last_placement_ascii
                    inner_break = False
                    
                    for xd2 in "abcdefghijkl":
                        if time_cutoff and time.time() - start > max_time:
                            break
                        for yd2 in range(1,11):
                            if time_cutoff and time.time() - start > max_time:
                                break
                            # placement
                            if data.get_active_placement_count() < data.max_tokens:
                                controller.game_loop(str(xd2) + str(yd2), True)
                                if data.get_error_message() == "unset":
                                    h = evaluate_heuristic(data.board)
                                    #print(str(alpha) + " " + str(beta) + " " + str(h) + " " + "p." + str(xd2) + '.' + str(yd2))
                                    if h < alpha:
                                        alpha = h
                                    if alpha < beta:
                                        inner_break = True
                                        break 
                                    #print(alpha)
                                    #print(beta)
                                    data.board = np.copy(store_board_d1)
                                    data.player_data = np.copy(store_player_data_d1)
                                    data.win_state = store_win_state_d1
                                    data.last_placement_ascii = store_last_placement_ascii_d1
                            else:
                                for xdm2 in "abcdefghijkl":
                                    if time_cutoff and time.time() - start > max_time:
                                        break
                                    for ydm2 in range(1,11):
                                        if time_cutoff and time.time() - start > max_time:
                                            break
                                        if data.board[10 - yd2][ord(xd2) - 97] == data.get_active_player_ascii():
                                            controller.game_loop(str(xd2) + str(yd2) +  ' ' + str(xdm2) +  str(ydm2), True)
                                            if data.get_error_message() == "unset":
                                                h = evaluate_heuristic(data.board) - move_heuristic
                                                if h < alpha:
                                                    alpha = h 
                                                if alpha < beta:
                                                    inner_break = True
                                                    break
                                                
                                                data.board = np.copy(store_board_d1)
                                                data.player_data = np.copy(store_player_data_d1)
                                                data.win_state = store_win_state_d1
                                                data.last_placement_ascii = store_last_placement_ascii_d1    
                                    if inner_break:
                                        break
                               
                            data.error_msg = "unset"
                            
                        if inner_break:
                            break
                    if alpha > beta:
                        beta = alpha
                        current_best_move = str(xd1) + str(yd1)
                    alpha = float("inf")
                    data.board = np.copy(store_board_d0)
                    data.player_data = np.copy(store_player_data_d0)
                    data.win_state = store_win_state_d0
                    data.last_placement_ascii = store_last_placement_ascii_d0
                    data.error_msg = "unset"  
                data.error_msg = "unset"  
            else:
                # movement
                for xdm1 in "abcdefghijkl":
                    if time_cutoff and time.time() - start > max_time:
                        break
                    for ydm1 in range(1,11):
                        if time_cutoff and time.time() - start > max_time:
                            break
                        if data.board[10 - yd1][ord(xd1) - 97] == data.get_active_player_ascii():
                            exit_reached = not controller.game_loop(str(xd1) + str(yd1) + " " + str(xdm1) + str(ydm1), True)
                            if data.get_error_message() == "unset":
                                resign_case_move = str(xd1) + str(yd1) + " " + str(xdm1) + str(ydm1)
                                if data.win_state != "unset":
                                    exit_reached = True
                                if exit_reached:
                                    data.error_msg = "unset"  
                                    data.board = np.copy(store_board_d0)
                                    data.player_data = np.copy(store_player_data_d0)
                                    data.win_state = store_win_state_d0
                                    data.last_placement_ascii = store_last_placement_ascii_d0     
                                    print("exit")
                                    print(str(xd1) + str(yd1) + " " + str(xdm1) + str(ydm1))
                                    return str(xd1) + str(yd1) + " " + str(xdm1) + str(ydm1)
                                store_board_d1 = np.copy(data.board)
                                store_player_data_d1 = np.copy(data.get_raw_player_data())
                                store_win_state_d1 = data.win_state
                                store_last_placement_ascii_d1 = data.last_placement_ascii
                                inner_break = False
                                
                                for xd2 in "abcdefghijkl":
                                    if time_cutoff and time.time() - start > max_time:
                                        break
                                    for yd2 in range(1,11):
                                        if time_cutoff and time.time() - start > max_time:
                                            break
                                        if data.get_active_placement_count() < data.max_tokens:
                                            controller.game_loop(str(xd2) + str(yd2), True)
                                            if data.get_error_message() == "unset":
                                                h = evaluate_heuristic(data.board) + move_heuristic
                                                if h < alpha:
                                                    alpha = h
                                                if alpha < beta:
                                                    inner_break = True
                                                    break 
                                                
                                                data.board = np.copy(store_board_d1)
                                                data.player_data = np.copy(store_player_data_d1)
                                                data.win_state = store_win_state_d1
                                                data.last_placement_ascii = store_last_placement_ascii_d1
                                        else:
                                            for xdm2 in "abcdefghijkl":
                                                if time_cutoff and time.time() - start > max_time:
                                                    break
                                                for ydm2 in range(1,11):
                                                    if time_cutoff and time.time() - start > max_time:
                                                        break
                                                    if data.board[10 - yd2][ord(xd2) - 97] ==  data.get_active_player_ascii():
                                                        controller.game_loop(str(xd2) + str(yd2) + " " + str(xdm2) + str(ydm2), True)
                                                        if data.get_error_message() == "unset":
                                                            h = evaluate_heuristic(data.board) - move_heuristic
                                                            if h < alpha:
                                                                alpha = h
                                                            if alpha < beta:
                                                                inner_break = True
                                                                break 
                                                            
                                                            data.board = np.copy(store_board_d1)
                                                            data.player_data = np.copy(store_player_data_d1)
                                                            data.win_state = store_win_state_d1
                                                            data.last_placement_ascii = store_last_placement_ascii_d1    
                                                if inner_break:
                                                    break
                                            data.error_msg = "unset"
                                    if inner_break:
                                        break        
                                        
                                if alpha > beta:
                                    beta = alpha
                                    current_best_move = str(xd1) + str(yd1) + " " + str(xdm1) + str(ydm1)
                                alpha = float("inf")
                                data.board = np.copy(store_board_d0)
                                data.player_data = np.copy(store_player_data_d0)
                                data.win_state = store_win_state_d0
                                data.last_placement_ascii = store_last_placement_ascii_d0
                        data.error_msg = "unset"  
                data.error_msg = "unset"  
        data.error_msg = "unset"  
    data.error_msg = "unset"  
    data.board = np.copy(store_board_d0)
    data.player_data = np.copy(store_player_data_d0)
    data.win_state = store_win_state_d0
    data.last_placement_ascii = store_last_placement_ascii_d0        
    if current_best_move == "RESIGN":
        current_best_move = resign_case_move
    print(current_best_move + " " + str(alpha) + " " + str(beta) + " " + str(time.time() - start))
    return current_best_move

    
if __name__ == "__main__":
    start = time.time()
    t1 = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]])
    data.board = t1
    print(evaluate_heuristic(t1))
    print(t1)
    end = time.time()
    print(end - start)
