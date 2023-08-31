from pathlib import Path
import json
import time
# Julian Aparicio
# japaric4@uci.edu
# 74237345
# Profile.py
#
# ICS 32
# Assignment #2: Journal
#
# Author: Mark S. Baldwin, modified by Alberto Krone-Martins
#
# v0.1.9

# You should review this code to identify what features you need to support
# in your program for assignment 2.
#
# YOU DO NOT NEED TO READ OR UNDERSTAND
# THE JSON SERIALIZATION ASPECTS OF THIS CODE
# RIGHT NOW, though can you certainly
# take a look at it if you are curious since we
# already covered a bit of the JSON format in class.
#
class Profile:
    """
    The Profile class exposes the
    properties required to join an ICS 32 DSU server. You
    will need to use this class to
    manage the information provided by each new user
    created within your program for
    a2. Pay close attention to the properties and
    functions in this class as you will need to make
    use of each of them in your program.

    When creating your program you
    will need to collect user input for the properties
    exposed by this class. A
    Profile class should ensure that a username and password
    are set, but contains no
    conventions to do so. You should make sure that your code
    verifies that required properties are set.

    """

    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.messages = {'messages': []}
        self.contacts = []
        self.new = []


    def add_new(self, msg):
        self.new.append(msg)


    def add_cont1(self, contact):
        '''
        This adds contacts to the contact list so every time the user loads their profile, their contacts are automatically added into the tree view menu.
        '''
        self.contacts.append(contact)


    def add_message(self, message):
        '''
        This message messages into the self.message list so that messages are stored locally.
        '''
        self.messages['messages'].append(message)


    """

    save_profile accepts an existing dsu file to save the
    current instance of Profile
    to the file system.

    Example usage:

    profile = Profile()
    profile.save_profile('/path/to/file.dsu')

    Raises DsuFileError

    """
    def save_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as ex:
                pass

    """

    load_profile will populate the current
    instance of Profile with data stored in a
    DSU file.

    Example usage:

    profile = Profile()
    profile.load_profile('/path/to/file.dsu')

    Raises DsuProfileError, DsuFileError

    """
    def load_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.messages = obj['messages']
                self.contacts = obj['contacts']
                self.new = obj['new']
                f.close()
            except Exception as ex:
                pass
