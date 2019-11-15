def d3_find_best_solution(min):
    global depth
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"
    current_best_heuristic = 0
    board = statespacegenerator.return_storable_board(data.get_board())
    if depth < precomputed_depth and hasattr(statespacedepth3, 's_' + board):
        opening_list = eval("statespacedepth3.s_" + board)
    else:
        # not found. create connections
        opening_list = find_connections(board)
    opening_index = 0
    for connection_1 in opening_list:
        if opening_index == 0:
            opening_index += 1
            continue
        if depth < precomputed_depth and hasattr(statespacedepth3, 's_' + str(connection_1)):
            connection_1_list = eval("statespacedepth3.s_" + str(connection_1))
        else:
            # not found. create connections
            connection_1_list = find_connections(connection_1)
        conn_1_index = 0
        for connection_2 in connection_1_list:
            if conn_1_index == 0:
                conn_1_index += 1
                continue
            if depth < precomputed_depth and hasattr(statespacedepth3, 's_' + str(connection_2)):
                connection_2_list = eval("statespacedepth3.s_" + str(connection_2))
            else:
                # not found. create connections
                connection_2_list = find_connections(connection_2)
            conn_2_index = 0
            for connection_3 in connection_2_list:
                if conn_2_index == 0:
                    conn_2_index += 1
                    continue
                h = evaluate_heuristic(statespacegenerator.return_numpy_board(str(connection_3)))
                if min and h <= current_best_heuristic:
                    current_best_move = connection_1_list[0]
                    current_best_heuristic = h 
                elif max and h >= current_best_heuristic:
                    current_best_move = connection_1_list[0]
                    current_best_heuristic = h
    return current_best_move
    
def d2_find_best_solution(min):
    global depth
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"
    current_best_heuristic = 0
    board = statespacegenerator.return_storable_board(data.get_board())
    if depth < precomputed_depth and hasattr(statespacedepth3, 's_' + board):
        opening_list = eval("statespacedepth3.s_" + board, 0, 0)
    else:
        # not found. create connections
        opening_list = find_connections(board)
    opening_index = 0
    for connection_1 in opening_list:
        if opening_index == 0:
            opening_index += 1
            continue
        if depth < precomputed_depth and hasattr(statespacedepth3, 's_' + str(connection_1)):
            connection_1_list = eval("statespacedepth3.s_" + str(connection_1))
        else:
            # not found. create connections
            opening_list
            connection_1_list = find_connections(connection_1)
        conn_2_index = 0
        for connection_2 in connection_1_list:
            if conn_2_index == 0:
                conn_2_index += 1
                continue
            h = evaluate_heuristic(statespacegenerator.return_numpy_board(str(connection_2)))
            if min and h <= current_best_heuristic:
                current_best_move = connection_1_list[0]
                current_best_heuristic = h 
            elif max and h >= current_best_heuristic:
                current_best_move = connection_1_list[0]
                current_best_heuristic = h
    return interpret_move(current_best_move)    
    
    
    
    

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
                        h += 1
                        
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
                        h += 1
                        
                if y - 1 >= 0:
                    if board[y - 1][x] == opposing_ascii:
                        h -= 2
                    elif board[y - 1][x] == active_ascii:
                        h += 1
                        
                if x + 1 < 12 and y + 1 < 10:
                    if board[y + 1][x + 1] == opposing_ascii:
                        h -= 1
                    elif board[y + 1][x + 1] == active_ascii:
                        h += 1
                        
                if x + 1 < 12:
                    if board[y][x + 1] == opposing_ascii:
                        h -= 2
                    elif board[y][x + 1] == active_ascii:
                        h += 1
                        
                if x + 1 < 12 and y - 1 < 10:
                    if board[y - 1][x + 1] == opposing_ascii:
                        h -= 1
                    elif board[y - 1][x + 1] == active_ascii:
                        h += 1
    return h

def find_connections(board_state, swap_active):

    propper_board = np.copy(data.get_board())
    if swap_active:
        data.reverse_player_data()
    board_state_decomp = board_state.split("9")
    if board_state_decomp[0] == "1":
        data.increment_active_placement_count()
    elif board_state_decomp[0] == "2":
        data.increment_active_move_count()
        
    open_list = queue.Queue()
    open_list.put(board_state_decomp[1])
    
    
    data.board = statespacegenerator.return_numpy_board(board_state_decomp[1])
    data.error_msg = "unset"
    statespace_holder_dict = {}
    statespace_holder_dict[board_state_decomp[1]] = {
        "player_data": np.copy(data.player_data), 
        "error_msg": data.error_msg, 
        "win_state": data.win_state, 
        "last_placement_ascii": data.last_placement_ascii,
        "connections" : [],
        "operations" : []
    }

    depth = 0
    conn_no_depth = 0
    depth_increment_point = 0
    connections_past = 0
    depth_flag = False
    depth_cuttoff = 1

    while not open_list.empty():
        head_node = open_list.get()
        for x in "abcdefghijkl":
            for y in range(1,11):
                data.board = statespacegenerator.return_numpy_board(head_node)
                data.player_data = np.copy(statespace_holder_dict[head_node]["player_data"])    
                data.error_msg = statespace_holder_dict[head_node]["error_msg"]        
                data.win_state = statespace_holder_dict[head_node]["win_state"]        
                data.last_placement_ascii = statespace_holder_dict[head_node]["last_placement_ascii"]              
                controller.game_loop("p." + str(x) + '.' + str(y), True)
                if data.error_msg == "unset":
                    # write board state into placeholder dict
                    conn_board = "19" + statespacegenerator.return_storable_board(data.get_board())
                    statespace_holder_dict[head_node]["connections"].append(conn_board)
                    statespace_holder_dict[head_node]["operations"].append("19" + str(format(ord(x)-96, 'o')) + '9' + str(format(y, 'o')))
                    statespace_holder_dict[conn_board] = {
                        "player_data": np.copy(data.player_data), 
                        "error_msg": data.error_msg, 
                        "win_state": data.win_state, 
                        "last_placement_ascii": data.last_placement_ascii,
                        "connections" : [],
                        "operations" : []
                    }
                    open_list.put(conn_board)
        # now for all the moves
        search_piece = "1"
        if data.get_active_player_ascii == data.p1_ascii:
            search_piece = "2"  
        else:
            search_piece = "3"
        ind = 0
        for spot in "head_node":
            if spot == search_piece:
                xi = ind / 12
                yi = ind % 12
                for xj in "abcdefghijkl":
                    for yj in range(1,11):
                        data.board = statespacegenerator.return_numpy_board(head_node)
                        data.player_data = np.copy(statespace_holder_dict[head_node]["player_data"])    
                        data.error_msg = statespace_holder_dict[head_node]["error_msg"]        
                        data.win_state = statespace_holder_dict[head_node]["win_state"]        
                        data.last_placement_ascii = statespace_holder_dict[head_node]["last_placement_ascii"]              
                        controller.game_loop("m." + str(xi) + '->' + str(xj) + '.' + str(yi) + '->' + str(yj), True)
                        if data.error_msg == "unset":
                            # write board state into placeholder dict
                            conn_board = "29" + statespacegenerator.return_storable_board(data.get_board())
                            statespace_holder_dict[head_node]["connections"].append(conn_board)
                            statespace_holder_dict[head_node]["operations"].append("29" + str(format(ord(xi)-96, 'o')) + '9' + str(format(ord(xj)-96, 'o')) + '9' + str(format(yi, 'o')) + '9' + str(format(yj, 'o')))
                            statespace_holder_dict[conn_board] = {
                                "player_data": np.copy(data.player_data), 
                                "error_msg": data.error_msg, 
                                "win_state": data.win_state, 
                                "last_placement_ascii": data.last_placement_ascii,
                                "connections" : [],
                                "operations" : []
                            }
                            open_list.put(conn_board)
        if depth_increment_point == conn_no_depth:
            depth = depth + 1
            depth_flag = True
        if depth_flag:
            depth_increment_point = open_list.qsize()
            depth_flag = False
        conn_no_depth += 1

        if depth == depth_cuttoff:
            break
            
    data.board = propper_board

    board_state_decomp = board_state.split("9")
    if board_state_decomp[0] == "1":
        data.decrement_active_placement_count()
    elif board_state_decomp[0] == "2":
        data.decrement_active_move_count()
    print(data.player_data)
    if swap_active:
        data.reverse_player_data()
        print(data.player_data)
    print("--")
    return statespace_holder_dict[board_state_decomp[1]]["operations"], statespace_holder_dict[board_state_decomp[1]]["connections"]


def d2_find_best_solution_no_store(min):
    global depth
    alpha = float("inf")
    beta = float("-inf")
    current_best_move = "RESIGN"
    current_best_heuristic = 0
    board = statespacegenerator.return_storable_board(data.get_board())

    _, opening_list = find_connections("09" + board, False)
    for connection_1 in opening_list:
        moves, connection_1_list = find_connections(connection_1, True)
        index = 0
        for connection_2 in connection_1_list:
            h = evaluate_heuristic(statespacegenerator.return_numpy_board(str(connection_2).split("9")[1]))
            if min and h <= current_best_heuristic:
                current_best_move = moves[index]
                current_best_heuristic = h 
            elif max and h >= current_best_heuristic:
                current_best_move = moves[index]
                current_best_heuristic = h
            index += 1
    if current_best_move != "RESIGN":
        return interpret_move(current_best_move)        
    else:
        return current_best_move
    
if __name__ == "__main__":
    start = time.time()
    print(d2_find_best_solution_no_store(False))

    end = time.time()
    print(end - start)