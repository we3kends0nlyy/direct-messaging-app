# Julian Aparicio
# japaric4@uci.edu
# 74237345
import json
import time
import ds_protocol
import re
import ds_client

class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None

    def recpt(self, recipient):
        self.recipient = recipient
        return self.recipient

class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.token = None
        self.port = 3021

    def send(self, message:str, recipient:str) -> bool:
        message_error = ds_client.mess_err_checker(self.dsuserver, self.port, self.username, self.password, message, "bio", recipient)
        if message_error is None:
            print("ERROR")
            print("Your message was not sent.")
            return False
        else:
            return message_error

    def retrieve_new(self) -> list:
        dict_mess = ds_client.req_err_checker(self.dsuserver, self.port, self.username, self.password, "new")
        if dict_mess is not None:
            msgs1 = []
            try:
                for i in range(len(dict_mess)):
                    directmessage = DirectMessage()
                    directmessage.timestamp = dict_mess[i]['timestamp']
                    directmessage.message = dict_mess[i]['message']
                    directmessage.recipient = dict_mess[i]['from']
                    msgs1.append(directmessage)
                return msgs1
            except TypeError:
                pass
        else:
            return dict_mess
        pass

    def retrieve_all(self) -> list:
        srv_msgg = ds_client.req_err_checker(self.dsuserver, self.port, self.username, self.password, "all")
        if srv_msgg is not None:
            msgss = []
            for i in range(len(srv_msgg)):
                directmessage = DirectMessage()
                directmessage.timestamp = srv_msgg[i]['timestamp']
                directmessage.message = srv_msgg[i]['message']
                directmessage.recipient = srv_msgg[i]['from']
                msgss.append(directmessage)
            return msgss
        else:
            return request_error
        pass
