# Julian Aparicio
# japaric4@uci.edu
# 74237345
from pathlib import Path
import re
import os
import a2
import ui
import checker
from Profile import *


def loaded(file_path):
    assign = Profile()
    assign.load_profile(file_path)
    print("Your contents have been loaded successfully!\n")
    print("Your username is: ", assign.username)
    print("Your password is: ", assign.password)
    print("Your bio is: ", assign.bio)
    print("")


def post_from_E(post, file_path):
    user_post = Post(entry=[post], timestamp=time.time())
    assign = Profile()
    assign.load_profile(file_path)
    assign.add_post(user_post)
    assign.save_profile(file_path)


def delete_post_E(num, file_path):
    assign = Profile()
    assign.load_profile(file_path)
    assign.del_post(num)
    assign.save_profile(file_path)


def save_from_e(usr, psw, bio, pst, dpst, file_path):
    lst_nums = []
    for i in range(100):
        lst_nums.append(i)
    assign = Profile()
    assign.load_profile(file_path)
    if len(usr) >= 1:
        assign.username = usr
        assign.save_profile(file_path)
        print("Your updated username is: ", usr)
    else:
        print("Your updated username is: ", usr)
    if len(psw) >= 1:
        assign.password = psw
        assign.save_profile(file_path)
        print("Your updated password is: ", psw)
    else:
        print("Your updated password is: ", psw)
    if len(bio) >= 1:
        assign.bio = bio
        assign.save_profile(file_path)
        print("Your updated bio is: ", bio)
    else:
        print("Your updated bio is: ", bio)
    if len(pst) >= 1:
        post_from_E(pst, file_path)
        print("Your latest post was: ", pst)
    else:
        print("You did not make a new post :(")
    if dpst in lst_nums:
        delete_post_E(dpst, file_path)
        try:
            pstt = assign.get_posts()[dpst]['entry']
            print("You deleted post #", dpst)
            print("Contents deleted: ", pstt[0])
        except IndexError:
            print("The index you deleted contained no post.")
            print("Nothing was deleted.")
    else:
        print("You did not delete any posts")


def user_asker(file_path, username, password, serv):
    with open(file_path, "w") as fp:
        pass
    assign = Profile()
    assign.save_profile(file_path)
    assign.dsuserver = serv
    assign.username = username
    assign.password = password
    #assign.bio = z
    assign.save_profile(file_path)
    '''
    x = input("Please input username:\n")
    if x == "Q":
        quit()
    elif x == "admin":
        a2.admin_func()
    match = re.search(r' ', x)
    if not match and len(x) > 0:
        y = input("Please enter a password:\n")
        if y == "Q":
            quit()
        elif y == "admin":
            a2.admin_func()
        else:
            match = re.search(r' ', y)
            if not match and len(y) > 0:
                option = input("Enter (B) for bio or (skip) to skip bio:\n")
                if option == "B":
                    z = input("Tell us something about yourself: \n")
                    print("Enter your DSU server number:")
                    print("Remember, once you input your DSU\
server you CANNOT", end="")
                    print(" go back and edit it.")
                    serv = input("Ok enter it now:\n")
                    myPath = Path(file_path)

                elif option == "skip":
                    print("That's ok, you can always add a bio later.")
                    serv = input("Enter your DSU server number:\n")
                    myPath = Path(file_path)
                    with open(os.path.join(pathe, serv_name), 'w') as fp:
                        pass
                    assign = Profile()
                    assign.save_profile(file_path)
                    assign.dsuserver = serv
                    assign.username = x
                    assign.password = y
                    assign.bio = ''
                    assign.save_profile(file_path)
                elif option == "Q":
                    quit()
                elif option == "admin":
                    a2.admin_func()
                else:
                    serv = input("Enter your DSU server number:\n")
                    myPath = Path(file_path)
                    with open(os.path.join(pathe, serv_name), 'w') as fp:
                        pass
                    assign = Profile()
                    assign.save_profile(file_path)
                    assign.dsuserver = serv
                    assign.username = x
                    assign.password = y
                    assign.bio = ''
                    assign.save_profile(file_path)
            else:
                print("Passwords must not have whitespace.")
                user_asker(file_path, pathe, serv_name)
    else:
        print("Usernames must not have whitespace.")
        user_asker(file_path, pathe, serv_name)
    '''
