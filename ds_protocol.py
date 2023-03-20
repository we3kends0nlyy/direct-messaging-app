# Julian Aparicio
# japaric4@uci.edu
# 74237345
import json
from collections import namedtuple
from Profile import *

DataTuple = namedtuple('DataTuple', ['foo', 'baz', 'bar'])
DataTuple2 = namedtuple('DataTuple', ['baz'])
DataTuple3 = namedtuple('DataTuple', ['baz'])
DataTuple4 = namedtuple('DataTuple', ['baz'])
DataTuple5 = namedtuple('DataTuple', ['baz'])
DataTuple6 = namedtuple('DataTuple', ['baz'])
DataTuple7 = namedtuple('DataTuple', ['baz'])


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
    '''
def extract_time(json_msg: str) -> DataTuple6:
    times = []
    try:
        json_obj = json.loads(json_msg)
        baz = json_obj['response']['messages']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return baz
    '''
def extract_sent(json_msg) -> DataTuple7:
    try:
        assign = Profile()
        baz = json_msg['directmessage']
        outside_list2 = []
        outout = []
        assign.load_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
        sent_msgs = {}
        outside_list2.append(sent_msgs)
        outout.append(outside_list2)
        try:
            if type(assign.messages[0][0]) is dict:
                try:
                    if len(assign.messages) == 1:
                        x = assign.messages
                        msg_list2 = []
                        msg_list2.append(baz)
                        sent_msgs[baz['recipient']] = msg_list2
                        final = []
                        final.append(outout)
                        assign.messages = final
                        assign.add_message(x)
                        assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
                except:
                    z = assign.messages
                    msg_list2 = []
                    msg_list2.append(baz)
                    try:
                        z[0][0][0][baz['recipient']] = msg_list2
                        assign.messages = z
                        assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
                    except:
                        msg_list2 = []
                        msg_list2.append(baz)
                        sent_msgs[baz['recipient']] = msg_list2
                        assign.add_message(outout)
                        assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
            elif type(assign.messages[0][0][0]) is dict:
                try:
                    if len(assign.messages[0][0][0][baz['recipient']]) > 0:
                        y = assign.messages
                        y[0][0][0][baz['recipient']].append(baz)
                        assign.messages = y
                        assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
                except KeyError:
                    msg_list2 = []
                    msg_list2.append(baz)
                    y = assign.messages
                    y[0][0][0][baz['recipient']] = msg_list2
                    assign.messages = y
                    assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
        except:
            msg_list2 = []
            msg_list2.append(baz)
            sent_msgs[baz['recipient']] = msg_list2
            assign.add_message(outout)
            assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/meme.dsu")
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return baz


def combine(msgs, users):
    '''
    user_list is a list of all the
    users that have sent messages
    to the user that's logged in.
    This list is used to iterate
    through the keys in my_dict.
    my_dict is a dictionary organized
    by user. Each front key is a user
    and each one has a list with
    all the posts organized by timestamp
    from that user. The "for u in users"
    for loop iterates through the
    users lists to create a list of
    users where the users are not
    repeated like they are in the users
    list. The "for i in range(len(msgs))"
    loop checks if a user has been added
    into the my_dict dictionary. If it
    is already in it, the message is
    added to that existing key. If the
    user hasn't been added, a new key
    is made and the message is put into
    that new key right after it's made.
    The most important feature is that
    I'm able to iterate through user_list
    and do "print(my_dict[j][0])" with j
    as the user from user_list. 0 gets
    the first message with the "from" the
    "timestamp" included which is really
    cool because I can access each post
    individually by specifying the index.
    So if a I'm logged in and have 10 posts
    from a certain user, I can do
    my_dict[j][7] to access the seventh
    post from that user. This will be useful
    when displaying all posts in order in the gui.
    '''
    assign = Profile()
    assign.load_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
    user_list = []
    outside_list = []
    for u in users:
        if u not in user_list:
            user_list.append(u)
    my_dict = {}
    outside_list.append(my_dict)
    for i in range(len(msgs)):
        if users[i] in my_dict:
            my_dict[users[i]].append(msgs[i])
        else:
            msg_list = []
            msg_list.append(msgs[i])
            my_dict[users[i]] = msg_list
    try:
        if type(assign.messages[1][0]) is dict:
            x = assign.messages[0]
            y = []
            y.append(x)
            assign.messages = y
            assign.add_message(outside_list)
            assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
        elif type(assign.messages[1][0][0]) is dict:
            print(assign.messages[0])
            print(assign.messages[1])
            new = []
            y = assign.messages[0]
            new.append(y)
            z = []
            z.append(outside_list)
            new.append(z)
            assign.messages = new
            assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
        else:
            assign.messages = assign.messages[1][0]
            assign.add_message(outside_list)
            assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
    except IndexError:
        try:
            if type(assign.messages[0][0]) is list:
                x = []
                x.append(outside_list)
                assign.add_message(x)
                assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
            elif type(assign.messages[0][0]) is dict:
                x = assign.messages
                assign.messages = x
                assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
            else:
                if type(assign.messages[0]) is dict:
                    x = assign.messages[1]
                    assign.messages.append(x)
                    assign.add_message(outside_list)
                    assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
                else:
                    assign.messages = outside_list
                    assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
        except:
            if type(assign.messages) is list:
                z = assign.messages
                assign.add_message(outside_list)
                assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/myjournal.dsu")
    '''
    for i in # the index that has the sent and received as two lists, index 0 and index 1, check if 'from' is a key inside because if it is then that's the messages received and that's what ill replace with my newest messages received, this way the messages sent will remain the same and the messages received wont be duplicated like theyre being right now.
    '''
    #except NameError:
        #assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/tetete.dsu")
    '''
    for j in user_list:
        print(len(my_dict[j]))
    print("TEST")
    quit()
    '''
