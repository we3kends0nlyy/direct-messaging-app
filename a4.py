# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Julian Aparicio
# japaric4@uci.edu
# 74237345
import post
import ui
global file_route

if __name__ == "__main__":
    COUNTER = 0
    x = input("Hello! Enter (C) to get started.\n")
    if x == "C":
        print("UI huh...U and I are going to go a looooong way my friend.")
        ui.greeting(COUNTER)
    elif x == "Q":
        quit()
    else:
        print("Hey friend, C is the magic code...please enter C to continue.")

    while x != "Q" or x == "admin":
        x = input("Enter (C) to continue. To quit, enter (Q).\n")
        if x == "Q":
            quit()
        elif x == "C":
            post.step2()
        else:
            print("C is the magic code...please enter C to continue.")
