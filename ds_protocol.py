# Julian Aparicio
# japaric4@uci.edu
# 74237345
import json
from collections import namedtuple
from Profile import *

DataTuple = namedtuple('DataTuple', ['foo', 'baz', 'bar'])
DataTuple3 = namedtuple('DataTuple', ['baz'])
DataTuple4 = namedtuple('DataTuple', ['baz'])
DataTuple5 = namedtuple('DataTuple', ['baz'])
DataTuple6 = namedtuple('DataTuple', ['baz'])
DataTuple7 = namedtuple('DataTuple', ['ba'])
DataTuple9 = namedtuple('DataTuple', ['baz'])


class SaveFilePath():

    def __init__(self, file_p):
        self.file_path = file_p


    def add_to_messages_rec(self, json_msg) -> DataTuple7:
        assign = Profile()
        assign.load_profile(self.file_path)
        new_list = []
        new_list.append(json_msg)
        if len(json_msg) > 0:
            assign.add_message(new_list)
            assign.save_profile(self.file_path)
        else:
            pass


    def add_to_messages_sent(self, json_msg) -> DataTuple7:
        baz = json_msg['directmessage']
        assign = Profile()
        assign.load_profile(self.file_path)
        new_list = []
        new_list.append(baz)
        new_list2 = []
        new_list2.append(new_list)
        if len(json_msg) > 0:
            assign.add_message(new_list2)
            assign.save_profile(self.file_path)
        else:
            pass


def extract_json(json_msg: str) -> DataTuple:
    try:
        json_obj = json.loads(json_msg)
        foo = json_obj['response']['token']
        baz = json_obj['response']['message']
        bar = json_obj['response']['type']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(foo, baz, bar)


def extract_json3(json_msg: str) -> DataTuple3:
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['message']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple3(baz)


def extract_user(json_msg: str) -> DataTuple5:
    users = []
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['messages']
        for i in range(len(baz)):
            users.append(baz[i]['from'])
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return users


def extract_json4(json_msg: str) -> DataTuple4:
    msgs = []
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['messages']
        boa = json_obj['response']['messages']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return baz
