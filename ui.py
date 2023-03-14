'''
This module is for the ui.
'''
# Julian Aparicio
# japaric4@uci.edu
# 74237345
import post


def greeting(counter):
    '''
    First greeting of the ui.
    '''
    counter += 1
    if counter > 1:
        post.step2()
    else:
        feeling = input("From 1-10, what would you rate McDonalds fries?\n")
        if feeling == "Q":
            quit()
        elif feeling == "":
            print("ERROR")
            greeting(counter)
        else:
            try:
                x_var = feeling.strip(" ")
                if len(x_var) > 0:
                    try:
                        num = int(feeling)
                        question(num)
                    except ValueError:
                        print("That wasn't an option. Have another go! :)")
                        greeting()
            except TypeError:
                print("ERROR")


def question(num):
    '''
    Question reply.
    '''
    if num <= 4:
        print("Too greasy, too salty, Red Robin fries are where it's at!")
        display_menu()
    elif num >= 5 and num < 7:
        print("They're mid, I agree.")
        display_menu()
    elif num == 7:
        print("Average McDonalds enjoyer.")
        display_menu()
    elif num in (8,9):
        print("You and Ronald McDonald go waayyy back.")
        display_menu()
    elif num == 10:
        print("Ok they're good, but not THAT good.")
        display_menu()


def display_menu():
    '''
    Displays the menu
    '''
    option = input("Enter (M) to display the menu:\n")
    if option == "M":
        post.step2()
    elif option == "Q":
        quit()
    else:
        print("Do you wanna see the menu or not???")
        display_menu()
