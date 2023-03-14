# Julian Aparicio
# japaric4@uci.edu
# 74237345
import json
from collections import namedtuple

DataTuple = namedtuple('DataTuple', ['foo', 'baz', 'bar'])
DataTuple2 = namedtuple('DataTuple', ['baz'])
DataTuple3 = namedtuple('DataTuple', ['baz'])
DataTuple4 = namedtuple('DataTuple', ['baz'])


def extract_json(json_msg: str) -> DataTuple:
    try:
        json_obj = json.loads(json_msg)
        foo = json_obj['response']['token']
        baz = json_obj['response']['message']
        bar = json_obj['response']['type']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(foo, baz, bar)


def extract_json2(json_msg: str) -> DataTuple2:
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['message']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple2(baz)


def extract_json3(json_msg: str) -> DataTuple3:
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['message']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple3(baz)

def extract_json4(json_msg: str) -> DataTuple4:
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['messages']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple3(baz)
