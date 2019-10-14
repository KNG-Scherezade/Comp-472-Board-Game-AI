"""MVC architecture for easy iterative development with data.py as a data file"""

import controller

print("Comp 472 AI Project :: X-RUDDER\nKAI NICOLL-GRIFFITH :: 40012407")
print("Type the number listed to play a certain game mode")
style = input("\t1\t- Human vs Human\n"
              "\t2\t- Human vs AI(work in progress)\n"
              "Enter a number: ")
if style == "1":
    while controller.run_human_routine(input("Perform a Placement, a Move (p.j.10 or m.a->b.1->2) or type RESIGN")):
        pass
print("X-Rudder done")
