'''
This is checker module that checks the command line inputs.
'''
# Julian Aparicio
# japaric4@uci.edu
# 74237345
from pathlib import Path
import re
import os
import user
import a2
from Profile import *
global file_route
from OpenWeather import OpenWeather
from LastFM import LastFM
import post


def file_route_store(fle):
    '''
    Stores the user file path as a global variable.
    '''
    global file_route
    file_route = fle


def fandr_checker(command):
    '''
    Checks for f and r in the command line.
    '''
    x = command.split(" ")
    if x[-1] == "-f" and x[-2] == "-r":
        spltcommand = command.split("L /")
        y2 = spltcommand[-1].split(" -r")
        new_string = "/" + y2[0]
        file = x[-1]
        return a2.func_file_recursion(new_string)
    else:
        rands_checker(command)


def rands_checker(command):
    '''
    Checks for r and s in the command line.
    '''
    x = command.split(" ")
    if x[-2] == "-s" and x[-3] == "-r":
        spltcommand = command.split("L /")
        y2 = spltcommand[-1].split(" -r")
        new_string = "/" + y2[0]
        file = x[-1]
        try:
            return a2.file_name_recursion(new_string, file)
        except IndexError:
            print("ERROR")
    else:
        rande_checker(command)


def rande_checker(command):
    '''
    Checks for r and e in the command line.
    '''
    x = command.split(" ")
    if x[-2] == "-e" and x[-3] == "-r":
        spltcommand = command.split("L /")
        y2 = spltcommand[-1].split(" -r")
        new_string = "/" + y2[0]
        ext = x[-1]
        try:
            return a2.extension_recursion(new_string, ext)
        except IndexError:
            print("ERROR")
    else:
        r_checker(command)


def r_checker(command):
    '''
    Checks for r in the command line.
    '''
    x = command.split("-")
    if x[-1] == "r":
        spltcommand = command.split("L /")
        y = spltcommand[-1].split(" -r")
        new_string = "/" + y[0]
        return a2.func_L_recursion(new_string)
    else:
        s_checker(command)


def s_checker(command):
    '''
    Checks for s in the command line.
    '''
    x = command.split(" ")
    if x[-2] == "-s":
        spltcommand = command.split("L /")
        y2 = spltcommand[-1].split(" -s")
        y = command.split(" ")
        fl = y[-1]
        new_string = "/" + y2[0]
        try:
            return a2.file_name_reader(new_string, fl)
        except IndexError:
            print("ERROR")
    else:
        e_checker(command)


def e_checker(command):
    '''
    Checks for e in the command line.
    '''
    x = command.split(" ")
    if x[-2] == "-e":
        spltcommand = command.split("L /")
        y = spltcommand[1].split(" ")
        ext = y[-1]
        y2 = spltcommand[-1].split(" -e")
        new_string = "/" + y2[0]
        try:
            return a2.extension_only(new_string, ext)
        except IndexError:
            print("ERROR")
    else:
        f_checker(command)


def f_checker(command):
    '''
    Checks for f in the command line.
    '''
    x = command.split("-")
    if x[-1] == "f":
        spltcommand = command.split("L /")
        y = spltcommand[-1].split(" -f")
        new_string = "/" + y[0]
        return a2.files_only(new_string)
    else:
        L_checker(command)


def L_checker(command):
    '''
    Checks for L in the command line.
    '''
    spltcommand = command.split("L /")
    try:
        new_string = "/" + spltcommand[1]
        return a2.func_all(new_string)
    except IndexError:
        print("ERROR")
        print("Index out of range")


def O_checker(command, choice):
    '''
    Checks for O in the command line.
    '''
    x = command.split(" ")
    if x[0] == "O":
        splt = command.split("O /")
        try:
            file_route = "/" + splt[1]
            dot = command.split(".")
            e = os.path.exists(file_route)
            if e is True:
                if dot[-1] != "dsu":
                    print("ERROR\nMust be a DSU file.")
                else:
                    post.store_file_route(file_route)
                    file_route_store(file_route)
                    if choice == "both":
                        post.O_loader_both_2(file_route)
                    elif choice == "bio":
                        post.O_loader_bio_2(file_route)
                    elif choice == "post":
                        post.O_loader_post_2(file_route)
                    elif choice == "load":
                        user.loaded(file_route)
            else:
                print("ERROR\nThat file does not exist.")
        except IndexError:
            print("ERROR")
            print("Index out of range")
    else:
        E_checker_usr(command)


def E_checker_usr(command):
    '''
    Checks for username in the E command.
    '''
    t = command.split(" -")
    if t[0] == "E":
        try:
            file_routes = file_route
            t = command.split(" ")
            match = re.search(r'-usr[" ""]', command)
            if match:
                inp = re.search(r'-usr ".*?"', command)
                try:
                    username = inp.group().split('"')[1]
                    usr1 = username
                    match = re.search(r' ', usr1)
                    if match:
                        print("ERROR")
                        print("Usernames must not contain whitespace.")
                    else:
                        E_checker_pwd(command, usr1, file_routes)
                except AttributeError:
                    print("ERROR")
                    print("Missing quotes around username.")
            else:
                usr1 = ''
                E_checker_pwd(command, usr1, file_routes)
        except NameError:
            print("ERROR")
            print("You must load a file first.")
    else:
        P_checker_usr(command)


def E_checker_pwd(command, usr1, file_routes):
    '''
    Checks for password in the E command.
    '''
    match = re.search(r'-pwd[" ""]', command)
    if match:
        find_pwd = re.search(r'-pwd ".*?"', command)
        try:
            password = find_pwd.group().split('"')[1]
            psw1 = password
            match = re.search(r' ', psw1)
            if match:
                print("ERROR")
                print("Passwords must not contain whitespace.")
            else:
                E_checker_bio(command, usr1, psw1, file_routes)
        except AttributeError:
            print("ERROR")
            print("Missing quotes around password.")
    else:
        psw1 = ''
        E_checker_bio(command, usr1, psw1, file_routes)


def E_checker_bio(command, usr1, psw1, file_routes):
    '''Checks for bio in the E command.
    '''
    match = re.search(r'-bio[" ""]', command)
    if match:
        find_bio = re.search(r'-bio ".*?"', command)
        try:
            bio = find_bio.group().split('"')[1]
            print("To update your bio to the server, enter (Y)")
            choice_bio = input("Otherwise, enter (N).\n")
            if choice_bio == "Y":
                post.bio_load_Y(bio, file_routes)
                E_checker_addpost(command, usr1, psw1, bio, file_routes)
            elif choice_bio == "Q":
                quit()
            elif choice_bio == "N":
                E_checker_addpost(command, usr1, psw1, bio, file_routes)
            else:
                print("ERROR")
        except AttributeError:
            print("ERROR")
            print("Missing quotes around bio.")
    else:
        bio = ''
        E_checker_addpost(command, usr1, psw1, bio, file_routes)


def save_api_info(lfm_api, ow_api, zip, ccode, artst):
    '''
    Saves api data as global.
    '''
    global lfm_api2
    lfm_api2 = lfm_api
    global ow_api2
    ow_api2 = ow_api
    global zip2
    zip2 = zip
    global ccode2
    ccode2 = ccode
    global artst2
    artst2 = artst


def E_checker_addpost(command, usr1, psw1, bio, file_routes):
    '''
    Checks for addpost and connects to the apis.
    '''
    match = re.search(r'-addpost[" ""]', command)
    if match:
        match_user = re.search(r'-addpost ".*?"', command)
        try:
            pst3 = match_user.group().split('"')[1]
        except AttributeError:
            print("ERROR")
            print("Missing quotes around post.")
        lfm_api_strip = lfm_api2.strip(" ")
        ow_api_strip = ow_api2.strip(" ")
        zip_strip = zip2.strip(" ")
        ccode_strip = ccode2.strip(" ")
        artist_strip = artst2.strip(" ")
        if len(artist_strip) > 0:
            artist3 = artst2.replace(" ", "+")
            lastfm = LastFM(artist3)
        else:
            lastfm = LastFM()
        if len(lfm_api_strip) > 0:
            lastfm.set_apikey(lfm_api2)
        else:
            lastfm.set_apikey("6f102f80b2272377724d86985c998d44")
        none_or1 = lastfm.load_data()
        if none_or1 is None:
            print("ERROR!!")
            print("Please enter valid data for the api.")
        else:
            result = lastfm.transclude(pst3)
            if len(zip_strip) > 0:
                if len(ccode_strip) > 0:
                    open_weather = OpenWeather(zip2, ccode2)
                else:
                    ccode3 = None
                    open_weather = OpenWeather(zip2, ccode3)
            else:
                if len(ccode_strip) > 0:
                    zip3 = None
                    open_weather = OpenWeather(zip3, ccode2)
                else:
                    open_weather = OpenWeather()
            if len(ow_api_strip) > 0:
                open_weather.set_apikey(ow_api2)
            else:
                open_weather.set_apikey("a1453ff49e7f356a69706971dafc160b")
            none_or2 = open_weather.load_data()
            if none_or2 is None:
                print("ERROR!")
                print("Please enter valid data for the api.")
            else:
                result2 = open_weather.transclude(result)
                if "None" not in result2:
                    print("To publish this post to the server, enter (Y)")
                    choice_2 = input("Otherwise, enter (N).\n")
                    if choice_2 == "Y":
                        E_checker_delpost(command, usr1, psw1, bio, result2, file_routes)
                        post.publish_post_only(result2, file_routes)
                    elif choice_2 == "Q":
                        quit()
                    elif choice_2 == "N":
                        E_checker_delpost(command, usr1, psw1, bio, result2, file_routes)
                    else:
                        print("ERROR")
                else:
                    print("ERROR")
                    print("Please enter valid data for the api.")
    else:
        pst3 = ''
        E_checker_delpost(command, usr1, psw1, bio, pst3, file_routes)



def E_checker_delpost(command, usr1, psw1, bio, pst1, file_routes):
    '''
    The last step in the E functions before calling save from e.
    '''
    match = re.search(r'-delpost[" 0-100000000000"]', command)
    if match:
        x_out = command.split("-delpost ")
        y = x_out[-1].split(" ")
        del1 = y[0]
        try:
            dell = int(del1)
            user.save_from_e(usr1, psw1, bio, pst1, dell, file_routes)
        except ValueError:
            print("ERROR\nYou must enter an integer following -delpost.")
            dell = ''
    else:
        del1 = ''
        try:
            user.save_from_e(usr1, psw1, bio, pst1, del1, file_routes)
        except NameError:
            print("Whoops! Looks like you hit an error.")


def P_checker_usr(command):
    '''
    P username checker.
    '''
    match = re.search(r'-usr', command)
    if match:
        assign = Profile()
        try:
            assign.load_profile(file_route)
            print(assign.username)
            P_checker_pwd(command)
        except NameError:
            print("ERROR")
            print("Must load file first.")
    else:
        P_checker_pwd(command)


def P_checker_pwd(command):
    '''
    P password checker.
    '''
    match = re.search(r'-pwd', command)
    if match:
        assign = Profile()
        try:
            assign.load_profile(file_route)
            print(assign.password)
            P_checker_bio(command)
        except NameError:
            print("ERROR")
            print("Must load file first.")
    else:
        P_checker_bio(command)


def P_checker_bio(command):
    '''
    P bio checker.
    '''
    match = re.search(r'-bio', command)
    if match:
        assign = Profile()
        try:
            assign.load_profile(file_route)
            print(assign.bio)
            P_checker_posts(command)
        except NameError:
            print("ERROR")
            print("Must load file first.")
    else:
        P_checker_posts(command)


def P_checker_posts(command):
    '''
    Checks for posts and prints all posts.
    '''
    match = re.search(r'-post[s]', command)
    if match:
        assign = Profile()
        try:
            assign.load_profile(file_route)
        except NameError:
            print("ERROR")
            print("Must load file first.")
        print("Here are your posts: ")
        for i in (range(len(assign.get_posts()))):
            pst = [assign.get_posts()[i]['entry']]
            x_out = str(pst)
            post = x_out.strip("[")
            post1 = post.strip("]")
            post2 = post1.strip("'")
            print(i, ":", post2)
    else:
        P_checker_post(command)


def P_checker_post(command):
    '''
    Check that post is in P and the index of it.
    '''
    match = re.search(r'-post', command)
    if match:
        x_out = command.split("-post ")
        y_out = x_out[-1].split(" ")
        del1 = y_out[0]
        dell = int(del1)
        assign = Profile()
        try:
            assign.load_profile(file_route)
            try:
                pstt = assign.get_posts()[dell]['entry']
                print("Your post is:")
                print(pstt[0])
            except IndexError:
                print("ERROR")
                print("Create a post first.")
        except NameError:
            print("ERROR")
            print("Must load file first.")
    else:
        P_checker_all(command)


def P_checker_all(command):
    '''
    Checks for P for print.
    '''
    t_out = command.split(" ")
    assign = Profile()
    if t_out[0] == "P":
        match = re.search(r'-all', command)
        if match:
            try:
                assign.load_profile(file_route)
                print("Username: ", assign.username)
                print("Password: ", assign.password)
                print("Bio: ", assign.bio)
                print("All posts: ")
                for i in (range(len(assign.get_posts()))):
                    pst = [assign.get_posts()[i]['entry']]
                    x_out = str(pst)
                    post = x_out.strip("[")
                    post1 = post.strip("]")
                    post2 = post1.strip("'")
                    print(i, ":", post2)
            except NameError:
                print("ERROR")
                print("Must load file first.")


def C_checker(command, choice):
    '''
    Checks the C command. This creates the new file.
    '''
    x_out = command.split(" ")
    if x_out[0] == "C":
        z = command.split(" ")
        spltcommand = command.split("C /")
        file_name = z[-1] + ".dsu"
        try:
            y = spltcommand[1].split(" ")
            y2 = spltcommand[-1].split(" -n")
            new_string = "/" + y2[0]
            new_path = new_string + "/" + file_name
            post.store_file_route(new_path)
            file_route_store(new_path)
            try:
                return a2.C_file_maker(new_string, file_name, new_path)
            except IndexError:
                print("ERROR")
        except IndexError:
            print("ERROR")
            print("Index out of range")
    else:
        O_checker(command, choice)


def D_checker(command, choice):
    '''
    Main D command checker.
    '''
    x_out = command.split(" ")
    if x_out[0] == "D":
        splt = command.split("D /")
        try:
            splt2 = "/" + splt[1]
            dot = command.split(".")
            if dot[-1] != "dsu":
                print("ERROR")
                DBackupChecker()
            else:
                return a2.file_delete(splt2)
        except IndexError:
            print("ERROR")
            print("Index out of range")
    else:
        read_checker(command, choice)


def DBackupChecker(command, choice):
    '''
    Backup checker for the D command.
    '''
    command2 = input()
    x_out = command2.split(" ")
    if x_out[0] == "D":
        splt = command2.split("D /")
        try:
            splt2 = "/" + splt[1]
            dot = command2.split(".")
            if dot[-1] != "dsu":
                print("ERROR")
                D_backup_checker()
            else:
                return a2.file_delete(splt2)
        except IndexError:
            print("ERROR")
            print("Index out of range")


def read_checker(command, choice):
    '''
    Main checker for read.
    '''
    x_out = command.split(" ")
    if x_out[0] == "R":
        splt = command.split("R /")
        try:
            splt2 = "/" + splt[1]
            dot = command.split(".")
            if dot[-1] != "dsu":
                print("ERROR")
                read_backup_checker()
            else:
                return a2.read_empty_checker(splt2)
        except IndexError:
            print("ERROR")
            print("Index out of range")
    else:
        C_checker(command, choice)


def read_backup_checker():
    '''
    Backup checker for read.
    '''
    command2 = input()
    if command2 == "Q":
        quit()
    else:
        x_out = command2.split(" ")
        if x_out[0] == "R":
            splt = command2.split("R /")
            try:
                splt2 = "/" + splt[1]
                dot = command2.split(".")
                if dot[-1] != "dsu":
                    print("ERROR")
                    read_backup_checker()
            except IndexError:
                print("ERROR")
                print("Index out of range")
            else:
                a2.read_empty_checker(splt2)
