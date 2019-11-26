
import heuristics
import heuristics_methods

import data 
import model 
import controller 
import numpy as np
import queue
import math
import time

time_cutoff = False
max_time = 4.98
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
    return h * heuristics.h0
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
                    h += heuristics.h1
                elif board[1,1] == opposing_ascii:
                    h +=  heuristics.h2
                else:
                    h += heuristics.h3
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h4
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h5
                else:
                    h += heuristics.h6          
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h7
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h8
                else:
                    h += heuristics.h9       
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h10
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h11
                else:
                    h += heuristics.h12
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h13
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h14
                else:
                    h += heuristics.h15          
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h16
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h17
                else:
                    h += heuristics.h18 
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h19
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h20
                else:
                    h += heuristics.h21
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h22
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h23
                else:
                    h += heuristics.h24          
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h25
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h26
                else:
                    h += heuristics.h27            
    elif board[0,0] == opposing_ascii:
        if board[0,1] == active_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h28
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h29
                else:
                    h += heuristics.h30
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h31
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h32
                else:
                    h += heuristics.h33          
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h34
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h35
                else:
                    h += heuristics.h36      
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h37
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h38
                else:
                    h += heuristics.h39
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h40
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h41
                else:
                    h += heuristics.h42         
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h43
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h44
                else:
                    h += heuristics.h45
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h46
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h47
                else:
                    h += heuristics.h48
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h49
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h50
                else:
                    h += heuristics.h51          
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h52
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h53
                else:
                    h += heuristics.h54
    else:
        if board[0,1] == active_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h55
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h56
                else:
                    h += heuristics.h57
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h58
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h59
                else:
                    h += heuristics.h60    
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h61
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h62
                else:
                    h += heuristics.h63 
        if board[0,1] == opposing_ascii:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h64
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h65
                else:
                    h += heuristics.h66
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h67
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h68
                else:
                    h += heuristics.h69         
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h70
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h71
                else:
                    h += heuristics.h72
        else:
            if board[1,0] == active_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h73
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h74
                else:
                    h += heuristics.h75
            elif board[1,0] == opposing_ascii:
                if board[1,1] == active_ascii:
                    h += heuristics.h76
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h77
                else:
                    h += heuristics.h78         
            else:
                if board[1,1] == active_ascii:
                    h += heuristics.h79
                elif board[1,1] == opposing_ascii:
                    h += heuristics.h80
                else:
                    h += heuristics.h81         
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
            h += heuristics.h82
    elif not(board[0,1] == active_ascii or board[2,1] == active_ascii or board[1,0] == active_ascii or board[1,2] == active_ascii):
        if (board[0,0] == opposing_ascii and board[1,1] == opposing_ascii and board[0,2] == opposing_ascii) or \
            (board[0,0] == opposing_ascii and board[1,1] == opposing_ascii and board[2,0] == opposing_ascii) or \
            (board[2,0] == opposing_ascii and board[1,1] == opposing_ascii and board[2,2] == opposing_ascii) or \
            (board[2,2] == opposing_ascii and board[1,1] == opposing_ascii and board[0,2] == opposing_ascii):
            h += heuristics.h83
    
    return h

def evaluate_heuristic(board):
    active_ascii = data.get_active_player_ascii()
    opposing_ascii = data.get_opposing_player_ascii()
    h = 0
    for x in range(0,12):
        for y in range(0,10):
            if data.board[y, x] != data.empty_ascii:
                h += twoway_convolution(board, y, x)
                h += threeway_convolution(board, y, x)
                h += positional_convolution(board, y, x) * 15 / data.get_both_placement_count()
    return h
     

def d2_find_best_solution_no_store():
    start = time.time()  
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"

    store_board_d0 = np.copy(data.board)
    store_player_data_d0 = np.copy(data.get_raw_player_data())
    store_win_state_d0 = data.win_state
    store_last_placement_ascii_d0 = data.last_placement_ascii
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
                    if data.win_state != "unset":
                        exit_reached = True
                    if exit_reached:
                        data.error_msg = "unset"  
                        data.board = np.copy(store_board_d0)
                        data.player_data = np.copy(store_player_data_d0)
                        data.win_state = store_win_state_d0
                        data.last_placement_ascii = store_last_placement_ascii_d0     
                        print("AI Wins")
                        heuristics_methods.write_heuristics()
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
                                                h = evaluate_heuristic(data.board)
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
                                                h = evaluate_heuristic(data.board)
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
                                                            h = evaluate_heuristic(data.board)
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
