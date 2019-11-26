"""
    Comp 472 AI Project :: X-RUDDER
    KAI NICOLL-GRIFFITH :: 40012407

    MVC architecture for easy iterative development with data.py as a data file.
    NumPy used for it's speed and the AI component

"""

import controller
import xrudderai
import data
import time

if __name__ == '__main__':

    print("Comp 472 AI Project :: X-RUDDER\nKAI NICOLL-GRIFFITH :: 40012407")
    print("Type the number listed to play a certain game mode")

    style = input("\t1\t- Human vs Human\n"
                  "\t2\t- Human vs AI(work in progress)\n"
                  "Enter a number: ")

    if style == "1":
        while controller.game_loop(input("Perform a Placement, a Move (p.j.10 or m.j->b.10->2) or type RESIGN: ")):
            pass
    elif style == "2":
        order = input("AI(1) or Human(2) first: ")
        game_active = True
        if order == "2":
            while game_active:
                if not controller.game_loop(input("Perform a Placement, a Move (p.j.10 or m.j->b.10->2) or type RESIGN: ")):
                    break
                while data.get_error_message() != "unset":
                    if not controller.game_loop(input("Perform a Placement, a Move (p.j.10 or m.j->b.10->2) or type RESIGN: ")):
                        break      
                if not controller.game_loop(xrudderai.d2_find_best_solution_no_store()):
                    break
        else:
            while game_active:
                if not controller.game_loop(xrudderai.d2_find_best_solution_no_store()):
                    break
                if not controller.game_loop(input("Perform a Placement, a Move (p.j.10 or m.j->b.10->2) or type RESIGN: ")):
                    break
                while data.get_error_message() != "unset":
                    if not controller.game_loop(input("Perform a Placement, a Move (p.j.10 or m.j->b.10->2) or type RESIGN: ")):
                        break
    elif style == "3":
        game_active = True
        while game_active:
            if not controller.game_loop(xrudderai.d2_find_best_solution_no_store()):
                break
            if not controller.game_loop(xrudderai.d2_find_best_solution_no_store()):
                break
    print("X-Rudder done")
