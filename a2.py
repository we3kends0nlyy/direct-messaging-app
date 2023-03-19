# Julian Aparicio
# japaric4@uci.edu
# 74237345

import post
from pathlib import Path
import re
import os
import ui
import user
import checker
import Profile


def extension_only(arg, file_ext):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if file_ext in currentPath.suffix:
                    print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def extension_recursion(arg, file_ext):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if file_ext in currentPath.suffix:
                    print(currentPath)
            elif (currentPath.is_dir()):
                recursion_extension_checker(currentPath, file_ext)
    except FileNotFoundError:
        print("ERROR")


def recursion_extension_checker(arg, file_ext2):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if file_ext2 in currentPath.suffix:
                    print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def file_name_reader(arg, file_name):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if currentPath.name == file_name:
                    print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def file_name_recursion(arg, file_name):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if currentPath.name == file_name:
                    print(currentPath)
            elif (currentPath.is_dir()):
                recursion_file_checker(currentPath, file_name)
    except FileNotFoundError:
        print("ERROR")


def recursion_file_checker(arg, file_name2):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                if currentPath.name == file_name2:
                    print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def func_L_recursion(arg):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if currentPath.is_file() and not ("/." in str(currentPath)):
                print(currentPath)
            elif (currentPath.is_dir()):
                print(currentPath)
                func_L_recursion(currentPath)
    except FileNotFoundError:
        print("ERROR")


def files_only(arg):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if currentPath.is_file() and not ("/." in str(currentPath)):
                print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def func_file_recursion(arg):
    try:
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_dir()):
                files_only(currentPath)
            elif currentPath.is_file() and not ("/." in str(currentPath)):
                print(currentPath)
    except FileNotFoundError:
        print("ERROR")


def func_all(arg):
    try:
        L_list = []
        myPath = Path(arg)
        for currentPath in myPath.iterdir():
            if (currentPath.is_file()):
                print(currentPath)
            elif (currentPath.is_dir()):
                L_list.append(currentPath)
        for i in range(len(L_list)):
            print(L_list[i])
    except FileNotFoundError:
        print("ERROR")


def C_file_maker(tha_path, file_name, new_path):
    myPath = Path(new_path)
    if (myPath.is_file()):
        open_file(new_path, new_path)
    else:
        with open(os.path.join(pathe, serv_name), 'w') as fp:
            pass


def print_new_file(pathe, name_file):
    myPath = Path(pathe)
    for currentPath in myPath.iterdir():
        if (currentPath.is_file()):
            if currentPath.name == name_file:
                print("Your file has been created!!!")
                print(currentPath)


def file_delete(pathe):
    try:
        os.remove(pathe)
        print(pathe + " DELETED")
    except FileNotFoundError:
        print("ERROR")


def read_empty_checker(filee):
    try:
        the_file = open(filee, "r")
        if os.path.getsize(filee) == 0:
            print("EMPTY")
        else:
            print(the_file.read(), end="")
    except FileNotFoundError:
        print("File does not exist.")


def open_file(filee, new_path):
    user.loaded(new_path)
    the_file = open(filee, "r")
    print("Inside your file:")
    print(the_file.read(), "\n")
