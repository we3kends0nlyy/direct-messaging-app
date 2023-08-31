# Julian Aparicio
# japaric4@uci.edu
# 74237345
from pathlib import Path
import re
import os
import a5
from Profile import *

def user_asker(file_path, username, password, serv):
    try:
        with open(file_path, "w") as fp:
            pass
        assign = Profile()
        assign.save_profile(file_path)
        assign.dsuserver = serv
        assign.username = username
        assign.password = password
        assign.save_profile(file_path)
        return True
    except OSError:
        a5.os_error()
