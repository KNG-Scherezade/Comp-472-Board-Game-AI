# Generate the state space for the AI to search and place into a .py file

import data 
import model 
import controller 
import numpy as np
import queue
import math
import time

start = time.time()

parent_board_state = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
statespace_holder_dict = {}
state_file = open("statespace.py", "w")

depth_cuttoff = 3

def return_storable_board(numpy_board):
    store = ""
    for x in numpy_board:
        for y in x:
            if y == data.empty_ascii:
                store = store + "1"
            elif y == 119:
                store = store + "2"  
            elif y == 114:
                store = store + "3"  
    return store

def return_numpy_board(storable_board):
    np_board = np.empty((10, 12), np.int8)
    itter_no = 0
    for chr in storable_board:
        no = 0
        if chr == "1":
            no = data.empty_ascii
        if chr == "2":
            no = 119       
        if chr == "3":
            no = 114   
        np_board[math.floor(itter_no / 12)][itter_no % 12] = no
        itter_no += 1
    return np_board

def states_into_memory():
    return


if __name__ == "__main__":
    open_list = queue.Queue()
    open_list.put(parent_board_state)

    statespace_holder_dict[parent_board_state] = {
        "player_data": np.copy(data.player_data), 
        "error_msg": data.error_msg, 
        "win_state": data.win_state, 
        "last_placement_ascii": data.last_placement_ascii,
        "operation" : "0",
        "connections" : []
    }

    depth = 0
    conn_no_depth = 0
    depth_increment_point = 0
    connections_past = 0
    depth_flag = False
    state_file.write("import numpy  as np\n\n")
    while not open_list.empty():
        head_node = open_list.get()
        for x in "abcdefghijkl":
            for y in range(1,11):
                data.board = return_numpy_board(head_node)
                data.player_data = np.copy(statespace_holder_dict[head_node]["player_data"])    
                data.error_msg = statespace_holder_dict[head_node]["error_msg"]        
                data.win_state = statespace_holder_dict[head_node]["win_state"]        
                data.last_placement_ascii = statespace_holder_dict[head_node]["last_placement_ascii"]              
                controller.game_loop("p." + str(x) + '.' + str(y), True)
                if data.error_msg == "unset":
                    # write board state into placeholder dict
                    conn_board = return_storable_board(data.get_board())
                    statespace_holder_dict[head_node]["connections"].append(conn_board)
                    statespace_holder_dict[conn_board] = {
                        "player_data": np.copy(data.player_data), 
                        "error_msg": data.error_msg, 
                        "win_state": data.win_state, 
                        "last_placement_ascii": data.last_placement_ascii,
                        "connections" : [],
                        "operation" : "19" + str(format(ord(x)-96, 'o')) + '9' + str(format(y, 'o'))
                    }
                    open_list.put(conn_board)
        # now for all the moves
        search_piece = "1"
        if data.get_active_player_ascii == 119:
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
                        data.board = return_numpy_board(head_node)
                        data.player_data = np.copy(statespace_holder_dict[head_node]["player_data"])    
                        data.error_msg = statespace_holder_dict[head_node]["error_msg"]        
                        data.win_state = statespace_holder_dict[head_node]["win_state"]        
                        data.last_placement_ascii = statespace_holder_dict[head_node]["last_placement_ascii"]              
                        controller.game_loop("m." + str(xi) + '->' + str(xj) + '.' + str(yi) + '->' + str(yj), True)
                        if data.error_msg == "unset":
                            # write board state into placeholder dict
                            conn_board = return_storable_board(data.get_board())
                            statespace_holder_dict[head_node]["connections"].append(conn_board)
                            statespace_holder_dict[conn_board] = {
                                "player_data": np.copy(data.player_data), 
                                "error_msg": data.error_msg, 
                                "win_state": data.win_state, 
                                "last_placement_ascii": data.last_placement_ascii,
                                "connections" : [],
                                "operation" : "29" + str(format(ord(xi)-96, 'o')) + '9' + str(format(ord(xj)-96, 'o')) + '9' + str(format(yi, 'o')) + '9' + str(format(yj, 'o'))
                            }
                            open_list.put(conn_board)
        if depth_increment_point == conn_no_depth:
            depth = depth + 1
            depth_flag = True
        if depth_flag:
            depth_increment_point = open_list.qsize()
            depth_flag = False
        conn_no_depth += 1
        state_file.write("s_" + head_node + " = np.array([" + statespace_holder_dict[head_node]["operation"] + ", " + \
        ",".join(statespace_holder_dict[head_node]["connections"]) + "], dtype=\"object\")\n")
        if depth == depth_cuttoff:
            end = time.time()
            print("d reached: " + str(depth))
            break
    end = time.time()
    print(end - start)
    state_file.close()
    exit()
    