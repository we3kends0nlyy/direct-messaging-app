# Julian Aparicio
# japaric4@uci.edu
# 74237345
from pathlib import Path
import re
import os
import ui
import user
import a2
from Profile import *
import ds_client
import checker


def store_file_route(fle):
    global file_route1
    file_route1 = fle


def step2():
    print("")
    print("~~~~~~~~~~~~~~~~~~MAIN MENU~~~~~~~~~~~~~~~~~~~~")
    print("<><><><><><><><><><><><><><><><><><><><><><><><>")
    print("---------------------Tips----------------------")
    print("Remember, you cannot send things to the")
    print("server that weren't already made in your profile.")
    print("You must load your profile")
    print("before posting or updating your bio on the server.")
    print("This can be done with the O command.")
    print("Which looks like this for example:")
    print("O /Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
    print("------------------MAIN OPTIONS-----------------")
    print("REMINDER:\nYou must edit your dsu profile", end=" ")
    print("with the E command then choose to", end=" ")
    print("publish your input to the server.")
    print("To create a new file, enter (C).")
    print("To edit an existing file, enter (E).")
    print(">>>>>>>HINT<<<<<<")
    print("To use the NEW API key feature, enter (E)!!!")
    print("To load an existing file, enter (O).")
    print("To publish an existing post AND bio online, enter (BOTH).")
    print("To publish ONLY a post online, enter (PO).")
    print("To update ONLY your bio online, enter (B).")
    print("To view the rest of the command", end="")
    x = input(" line inputs, enter (N).\n")
    if x == "Q":
        quit()
    elif x == "PO":
        assign = Profile()
        try:
            e = os.path.exists(file_route1)
            if e is True:
                assign.load_profile(file_route1)
                if len(assign._posts) > 0:
                    post_printer_only(file_route1)
                else:
                    print("ERROR")
                    print("You have no posts!")
                    print("Make a post using the E command.")
                    print("Then you can publish it to the server!")
            else:
                print("You must use the O command to load", end="")
                print("your DSU file before publishing.")
                O_loader_post()
        except NameError:
            print("You must use the O command to load", end="")
            print("your DSU file before publishing.")
            O_loader_post()
    elif x == "BOTH":
        assign = Profile()
        try:
            e = os.path.exists(file_route1)
            if e is True:
                assign.load_profile(file_route1)
                if len(assign._posts) > 0:
                    post_printer(file_route1)
                else:
                    print("ERROR")
                    print("You have no posts!")
                    print("Make a post using the E command.")
                    print("Then you can publish it to the server!")
            else:
                print("You must use the O command to load", end="")
                print("your DSU file before publishing.")
                O_loader_both()
        except NameError:
            print("You must use the O command to load", end="")
            print("your DSU file before publishing.")
            O_loader_both()
    elif x == "B":
        assign = Profile()
        try:
            e = os.path.exists(file_route1)
            if e is True:
                assign.load_profile(file_route1)
                user = assign.username
                pwd = assign.password
                bio = assign.bio
                server = assign.dsuserver
                p = None
                port = 3021
                bio_trigger(server, port, user, pwd, p, bio)
            else:
                print("You must use the O command to load", end="")
                print("your DSU file before publishing.")
                O_loader_bio()
        except NameError:
            print("You must use the O command to load", end="")
            print("your DSU file before publishing.")
            O_loader_bio()
    elif x == "N":
        choice = "load"
        choose(choice)
    elif x == "O":
        print("Example:")
        print("O /Users/we3kends0onlyy/Documents/TEST ING/filename.dsu")
        choice = "load"
        cmnd_line(choice)
    elif x == "C":
        choice = "load"
        print("Example:")
        print("C /Users/we3kends0onlyy/Documents/TEST ING -n", end="")
        print(" [Name of file](No .dsu needed here.)")
        cmnd_line(choice)
    elif x == "E":
        choice = "load"
        print("-------------OPTIONS OF THE E COMMAND-----------")
        print("E -usr  E -pwd  E -bio  E -addpost  E -delpost")
        print("You can use 1 or all commands at the same time.")
        print("When using more than one, you only need one E.")
        print("Example of multiple E commands called at once:")
        print("E -usr \"Julian\" -pwd \"123\" -bio \"bio\"", end="")
        print(" -addpost \"post!\" -delpost 3")
        print("-delpost has no quotations around it.")
        print(">>>>>NEW FEATURE!!!<<<<<<<")
        print("------------------------------------------------")
        print("There are now keywords that you can use from remote apis!")
        print("Here is the list of keywords you can use.")
        print("--------For the OpenWeather API-------")
        print("@weather = Description of the current weather of your area.")
        print("@temp = The current temperature of your area.")
        print("@lowtemp = The low temperature of your area.")
        print("@sunset = The sunset time of your area.")
        print("-----------For the LastFM API-----------")
        print("@lastfm = The genre of your artist.")
        print("@artistlisteners = The amount of listeners your artist has.")
        print("@artist = The name of your artist.")
        print("For example:")
        print("I love Irvine because it's @temp degrees today! I can blast my @lastfm all day!")
        print("Transludes to:")
        print("I love Irvine because it's 70 degrees today! I can blast my Hip Hop all day!")
        print("<><><><><><><><>")
        print("If you would like to enter your own api info, enter (A).")
        c = input("To continue with default values, enter (C).\n")
        if c == "A":
            print("You can choose to leave any of the following prompts blank.")
            print("You can do this by simply pressing enter when prompted.")
            print("If you leave the prompts blank, there are default values assigned.")
            ow_apikey = input("Please enter your OpenWeather api key.\n")
            zip = input("Enter a zip code.\n")
            print("Please enter a country code.\n")
            ccode = input("Example: US(United States), GB(England), ES(Spain).\n")
            lfm_apikey = input("Please enter your LastFM apikey.\n")
            print("Please enter the artist you'd like to use.")
            print("The first character must always be capitalized unless special case")
            artst = input("Example: Kanye West(Correct) kanye west(incorrect)\n")
            checker.save_api_info(lfm_apikey, ow_apikey, zip, ccode, artst)
            cmnd_line(choice)
        elif c == "Q":
            quit()
        elif c == "C":
            ow_apikey = "  "
            zip = "   "
            ccode = "   "
            lfm_apikey = "  "
            artst = "   "
            checker.save_api_info(lfm_apikey, ow_apikey, zip, ccode, artst)
            cmnd_line(choice)
        else:
            print("ERROR")
    else:
        print("ERROR")
        step2()


def choose(x):
    print("-----------------------------------------------")
    print("Choose from the list of commands.")
    print("Once you choose you will receive more detailed instructions.")
    print("L-List the contents of the specified directory.")
    print("D-Delete a file from a specified directory.")
    print("R-Read the contents of a file.")
    print("P-Print the contents of a dsu file.")
    print("Make your selection now.")
    print("Please enter one letter to continue:")
    letter = input("L/D/R/P\n")
    command_options(letter, x)


def command_options(letter, x):
    if letter == "L":
        print("Example of L command input:")
        print("L /Users/we3kends0onlyy/Documents/TESTING")
        print("Here TESTING is the folder destination.")
        print("That is the folder whose contents will be listed.")
        print("Options of the 'L' command")
        print("---------------------FORMAT--------------------")
        print("L /Users/we3kends0onlyy/Documents/TEST ING", end="")
        print("[\"-\"letter] [\"-\"optional second letter]")
        print("-r/Output directory content recursively.")
        print("-f/Output only files, excluding directories in the results.")
        print("-s/Output only files that match a given file name.")
        print("-e [ext]/Output only files that match a given file extension.")
        print("-r -f/Output files recursively.")
        print("-r -e jpeg/", end="")
        print("Output files with specified extension recursively.")
        print("-r -s [file.txt]", end=" ")
        print("Output files with the specified file name recursively.")
        print("Example:")
        print("L /Users/we3kends0onlyy/Documents/TEST ING -f")
        print("Example:")
        print("L /Users/we3kends0onlyy/Documents/TEST ING -e jpeg")
        print("Example:")
        print("L /Users/we3kends0onlyy/Documents/TEST ING -r -s file.txt")
        cmnd_line(x)
    elif letter == "D":
        print("Example:")
        print("D /Users/we3kends0onlyy/Documents/TEST ING/filename.dsu")
        cmnd_line(x)
    elif letter == "R":
        print("Example:")
        print("R /Users/we3kends0onlyy/Documents/TEST ING/filename.dsu")
        cmnd_line(x)
    elif letter == "P":
        print("-------------OPTIONS OF THE P COMMAND-------------")
        print("P -usr  P -pwd  P -bio  P -posts", end="")
        print("P -post [ID]  P -all\n")
        print("You can use 1 or all commands at the same time.")
        print("When using more than one, you only need one P.")
        print("Example of multiple P commands called at once:")
        print("P -usr -pwd -bio -post 3")
        cmnd_line(x)
    elif letter == "Q":
        quit()
    else:
        print("That wasn't an option.")


def O_loader_both():
    print("Please use O to load your posts now.")
    print("Example:")
    command = input("O /Users/we3kends0only/Documents/TESTING/myjournal.dsu\n")
    if command == "Q":
        quit()
    else:
        x = command.split(" /")
        if x[0] == "O":
            splt = command.split("O /")
            try:
                splt2 = "/" + splt[1]
                if os.path.exists(splt2) is True:
                    choice = "both"
                    checker.D_checker(command, choice)
                else:
                    print("The file you entered does not exist.")
                    print("Use the C command to create file.")
                    print("")
            except IndexError:
                print("ERROR")
        else:
            print("ERROR")


def O_loader_both_2(file_routecall):
    assign = Profile()
    assign.load_profile(file_route1)
    if len(assign._posts) > 0:
        print("Your file has been loaded successfully!")
        post_printer(file_routecall)
    else:
        print("ERROR")
        print("You have no posts!")
        print("Make a post using the E command.")
        print("Then you can publish it to the server!")


def O_loader_bio():
    print("Please use O to load your posts now.")
    print("Example:")
    command = input("O /Users/we3kends0only/Documents/TESTING/myjournal.dsu\n")
    if command == "Q":
        quit()
    else:
        x = command.split(" /")
        if x[0] == "O":
            splt = command.split("O /")
            try:
                splt2 = "/" + splt[1]
                if os.path.exists(splt2) is True:
                    choice = "bio"
                    checker.D_checker(command, choice)
                else:
                    print("The file you entered does not exist.")
            except IndexError:
                print("ERROR")
        else:
            print("ERROR")


def O_loader_bio_2(file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    user = assign.username
    pwd = assign.password
    bio = assign.bio
    server = assign.dsuserver
    p = None
    port = 3021
    bio_trigger(server, port, user, pwd, p, bio)


def bio_load_Y(bio, file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    user = assign.username
    pwd = assign.password
    bio1 = bio
    server = assign.dsuserver
    p = None
    port = 3021
    bio_trigger(server, port, user, pwd, p, bio1)


def post_printer_only(file_route1):
    try:
        assign = Profile()
        assign.load_profile(file_route1)
        print("Here are your posts: ")
        for i in (range(len(assign.get_posts()))):
            pst = [assign.get_posts()[i]['entry']]
            x = str(pst)
            post = x.strip("[")
            post1 = post.strip("]")
            post2 = post1.strip("'")
            print(i, ":", post2)
        choose_post_only(file_route1)
    except NameError:
        print("ERROR")


def choose_post_only(file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    num = input("Please choose a post number to publish\n")
    if num == "Q":
        quit()
    else:
        try:
            num1 = int(num)
            try:
                pstt = assign.get_posts()[num1]['entry']
                publish_post_only(pstt[0], file_route1)
            except IndexError:
                print("ERROR")
                print("That post doesn't exist.")
                print("Please choose another post.")
        except ValueError:
            print("ERROR")
            print("Must be an integer.")
            choose_post_only(file_route1)


def publish_post_only(post, file_path):
    assign = Profile()
    assign.load_profile(file_path)
    user = assign.username
    pwd = assign.password
    server = assign.dsuserver
    p = post
    port = 3021
    post_trigger(server, port, user, pwd, p)


def O_loader_post():
    print("Please use O to load your posts now.")
    print("Example:")
    command = input("O /Users/we3kends0only/Documents/TESTING/myjournal.dsu\n")
    if command == "Q":
        quit()
    else:
        x = command.split(" /")
        if x[0] == "O":
            splt = command.split("O /")
            try:
                splt2 = "/" + splt[1]
                if os.path.exists(splt2) is True:
                    x = "post"
                    checker.D_checker(command, x)
                else:
                    print("The file you entered does not exist.")
            except IndexError:
                print("ERROR")
        else:
            print("ERROR")


def O_loader_post_2(file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    if len(assign._posts) > 0:
        print("Your file has been loaded successfully!")
        print(file_route1)
        post_printer_only(file_route1)
    else:
        print("ERROR")
        print("You have no posts!")
        print("Make a post using the E command.")
        print("Then you can publish it to the server!")


def post_trigger(server, port, user, pwd, p):
    trig = input("To publish your post, enter GO.\n")
    if trig == "GO":
        ds_client.send(server, port, user, pwd, p)
    elif trig == "Q":
        quit()
    else:
        print("Please enter (GO) to proceed")
        post_trigger(server, port, user, pwd, p)


def bio_trigger(server, port, user, pwd, p, bio):
    trig = input("To update your bio, enter (U).\n")
    if trig == "U":
        ds_client.send(server, port, user, pwd, p, bio)
    elif trig == "Q":
        quit()
    else:
        print("Please enter (U) to proceed")
        bio_trigger(server, port, user, pwd, p, bio)


def post_printer(file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    try:
        print("Here are your posts: ")
        for i in (range(len(assign.get_posts()))):
            pst = [assign.get_posts()[i]['entry']]
            x = str(pst)
            post = x.strip("[")
            post1 = post.strip("]")
            post2 = post1.strip("'")
            print(i, ":", post2)
        choose_post(file_route1)
    except NameError:
        print("ERROR")


def choose_post(file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    num = input("Please choose a post number to publish\n")
    if num == "Q":
        quit()
    else:
        try:
            num1 = int(num)
            try:
                pstt = assign.get_posts()[num1]['entry']
                publish(pstt[0], file_route1)
            except IndexError:
                print("This post doesn't exist")
                print("ERROR")
        except ValueError:
            print("ERROR")
            print("Must be an integer.")
            choose_post(file_route1)


def publish(post, file_route1):
    assign = Profile()
    assign.load_profile(file_route1)
    user = assign.username
    pwd = assign.password
    bio = assign.bio
    server = assign.dsuserver
    p = post
    port = 3021
    ds_client.send(server, port, user, pwd, p, bio)


def cmnd_line(x):
    global command
    command = input("Please enter your command line input now.\n")
    if command == "Q":
        quit()
    else:
        let = input("Currently loading your input so pick a letter A or B.\n")
        if let == "A":
            print("Almost there...")
            last_step(command, x)
        elif let == "B":
            print("Hey be patient I'm workin here!")
            last_step(command, x)
        elif let == "Q":
            quit()
        else:
            print("You didn't choose A or B, so I'll C you later!!")
            last_step(command, x)


def last_step(command, x):
    trigger = input("When you want your input to be executed, enter (GO).\n")
    if trigger == "GO":
        match = re.search(r'L[" "]', command)
        if match:
            checker.fandr_checker(command)
        elif len(command) < 2:
            print("ERROR")
        else:
            checker.D_checker(command, x)
    elif trigger == "Q":
        quit()
    else:
        print("It seems you messed up your spelling. Please try again.")
        last_step(command, x)
