# Julian Aparicio
# japaric4@uci.edu
# 74237345
import socket
import json
import time
import ds_protocol
from ds_protocol import SaveFilePath
import re
import a5


def save_path(p):
    global path
    path = p


def user_pass_checker(username, password):
    try:
        if len(username) > 0 and len(password) > 0:
            match = re.search(r' ', username)
            if match:
                a5.space_error()
                print("ERROR\nUsername can't have whitespace.")
                return False
            else:
                match = re.search(r' ', password)
                if match:
                    print("ERROR\nPassword can't have whitespace.")
                    return False
                else:
                    return True
        else:
            print("ERROR\nUsername or password is empty.")
            return False
    except Exception as e:
        print(e)
        print("ERROR\nUsername and password must be strings.")
        return False


def send_2(server: str, port: int, username: str, password: str, request: str):
    request_error = req_err_checker(server, port, username, password, request)
    if request_error is None:
        return request_error
    else:
        return request_error


def req_err_checker(server, port, username, password, request):
    use = user_pass_checker(username, password)
    if use is True:
        returned = req_mess(server, port, username, password, request)
        return returned
    else:
        return use


def req_mess(server, port, username, password, request):
    try:
        y = request.strip(" ")
        if len(y) > 0:
            mess = connect(server, port, username, password, request)
            if mess is not False:
                if request is "new":
                    returned = req_msgs_new(server, port, username, password, request, mess[1], mess[2], mess[0])
                    return returned
                if request is "all":
                    returned = req_msgs_all(server, port, username, password, request, mess[1], mess[2], mess[0])
                    return returned
            else:
                return mess
        else:
            print("ERROR\nRequest can't be whitespace only.")
            return False
    except AttributeError:
        return None


def req_msgs_new(server, port, username, password, request, test, recv, x):
    real_msg = {"token": x[0], "directmessage": request}
    j = to_json(real_msg)
    while True:
        test.write(j + '\r\n')
        test.flush()
        srv_msg = recv.readline()[:-1]
        sfp = SaveFilePath(path)
        msg = ds_protocol.extract_json4(srv_msg)
        return msg


def req_msgs_all(server, port, username, password, request, test, recv, x):
    real_msg = {"token": x[0], "directmessage": request}
    j = to_json(real_msg)
    while True:
        test.write(j + '\r\n')
        test.flush()
        srv_msg = recv.readline()[:-1]
        sfp = SaveFilePath(path)
        msg = ds_protocol.extract_json4(srv_msg)
        user = ds_protocol.extract_user(srv_msg)
        sfp.combine(msg, user)
        return msg


def send(server: str, port: int, username: str, password: str, message: str, recipient=None, bio: str = None):
    message_error = mess_err_checker(server, port, username, password, message, bio, recipient)
    if message_error is None:
        return_error = error_checker_bio(server, port, username, password, message, bio)
        if return_error is None:
            return_error2 = error_checker_post(server, port, username, password, message, bio)
            if return_error2 is None:
                return_error3 = error_checker_post_bio(server, port, username, password, message, bio)
                return return_error3
            else:
                print("")
                return return_error2
        else:
            return return_error
    else:
        return message_error


def mess_err_checker(server, port, username, password, message, bio, recipient):
    '''
    This method calls the user_pass_checker method.
    If True is returned, the dir_mess method is
    called which is connected the msgs method.
    Once this line reaches the end, the result
    is either successfully sending a direct
    message to a user and returning True, or
    an error being caugnt along the
    way and returning False.
    '''
    use = user_pass_checker(username, password)
    if use is True:
        returned = dir_mess(server, port, username, password, message, bio, recipient)
        return returned
    else:
        return use


def dir_mess(server, port, username, password, message, bio, recipient):
    try:
        y = message.strip(" ")
        if len(y) > 0:
            try:
                x = recipient.strip(" ")
                if len(x) > 0:
                    mess = connect(server, port, username, password, message)
                    if mess is not False:
                        msgs(server, port, username, password, message, mess[1], mess[2], mess[0], recipient)
                        return True
                    else:
                        return mess
                else:
                    print("ERROR\nRecipient can't be whitespace only.")
                    return False
            except AttributeError:
                return None
        else:
            print("ERROR\nMessage can't be whitespace only.")
            return False
    except AttributeError:
        return None


def set_path(pa):
    global f_path
    f_path = pa


def msgs(server, port, username, password, message, test, recv, x, recipient):
    real_msg = {"token": x[0], "directmessage": {"entry": message,"recipient": recipient, "timestamp": time.time()}}
    j = to_json(real_msg)
    while True:
        test.write(j + '\r\n')
        test.flush()
        srv_msg = recv.readline()[:-1]
        #f_path = .ret_fp()
        fp = SaveFilePath(path)
        msg = ds_protocol.extract_json3(srv_msg)
        msg_store = fp.extract_sent(real_msg)
        break

def after_connect_join(server, port, test, recv, username, password, client):
    print(f"You are connected to server {server} on port {port}!")
    msg = {"join": {"username": username, "password": password, "token": ""}}
    j = to_json(msg)
    test.write(j + '\r\n')
    test.flush()
    msg = recv.readline()[:-1]
    return msg


def error_checker_bio(server, port, username, password, message, bio):
    if message is None:
        if bio is not None:
            if type(bio) == str:
                returned = bio_only(server, port, username, password, message, bio)
                return returned
            else:
                print("ERROR\nBio must be a string.")
                return False
        else:
            return False
    else:
        if type(message) != str:
            print("ERROR\nMessage must be a string.")
            return False
        else:
            pass


def error_checker_post(server, port, username, password, message, bio):
    if bio is not None:
        pass
    else:
        returned3 = post_only(server, port, username, password, message, bio)
        return returned3


def error_checker_post_bio(server, port, username, password, message, bio):
    try:
        y = bio.strip(" ")
        if len(y) > 0:
            returned2 = post_and_bio(server, port, username, password, message, bio)
            return returned2
        else:
            print("ERROR\nBio cant be whitespace only.")
            return False
    except AttributeError:
        print("ERROR")
        return False


def connect(server, port, username, password, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((server, port))
            test = client.makefile("w")
            recv = client.makefile("r")
            srv_msg = after_connect_join(server, port, test, recv, username, password, client)
            print(srv_msg)
            print("")
            if 'token' in srv_msg:
                x = ds_protocol.extract_json(srv_msg)
                print(f"{x[1]}! You're doing A {x[2]}!\nYour token number is: {x[0]}.")
                return [x, test, recv]
            else:
                print("ERROR\nToken not received.")
                print("Once a password is registered")
                print("with a user, you must always\nuse that same password.")
                a5.user_error()
                return False
        except (ConnectionRefusedError, TimeoutError, socket.gaierror, TypeError, OSError) as e:
            a5.connection_error()
            print("Connection error.")
            return False


def post_and_bio(server, port, username, password, message, bio):
    rtrn_p_b = connect(server, port, username, password, message)
    if rtrn_p_b is not False:
        post(server, port, username, password, message, rtrn_p_b[1], rtrn_p_b[2], rtrn_p_b[0], bio)
        bios(server, port, username, password, message, rtrn_p_b[1], rtrn_p_b[2], rtrn_p_b[0], bio)
        return True
    else:
        return rtrn_p_b


def post_only(server, port, username, password, message, bio):
    rtrn_p = connect(server, port, username, password, message)
    if rtrn_p is not False:
        post(server, port, username, password, message, rtrn_p[1], rtrn_p[2], rtrn_p[0], bio)
        return True
    else:
        return rtrn_p


def bio_only(server, port, username, password, message, bio):
    y = bio.strip(" ")
    if len(y) > 0:
        rtrn_b = connect(server, port, username, password, message)
        if rtrn_b is not False:
            bios(server, port, username, password, message, rtrn_b[1], rtrn_b[2], rtrn_b[0], bio)
            return True
        else:
            return rtrn_b
    else:
        print("ERROR\nBio can't be whitespace only.")
        return False


def post(server, port, username, password, message, test, recv, x, bio):
    post2 = {"token":x[0], "post": {"entry": message, "timestamp": "1603167689.3928561"}}
    j = to_json(post2)
    test.write(j + '\r\n')
    test.flush()
    srv_msg = recv.readline()[:-1]
    msg = ds_protocol.extract_json2(srv_msg)
    print(f"{msg[0]}!")
    print("Your latest post was: ", message)


def bios(server, port, username, password, message, test, recv, x, bio):
    bio3 = {"token": x[0], "bio": {"entry": bio, "timestamp": time.time()}}
    j = to_json(bio3)
    while True:
        test.write(j + '\r\n')
        test.flush()
        srv_msg = recv.readline()[:-1]
        msg = ds_protocol.extract_json2(srv_msg)
        print(f"{msg[0]}!")
        print("Your new bio is : ", bio)
        break


def to_json(obj: dict) -> str:
    jason = json.dumps(obj)
    return jason
