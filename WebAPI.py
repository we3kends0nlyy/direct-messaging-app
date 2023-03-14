'''
This module is the module that contains the
 base class for the OpenWeather and LastFM child classes.
'''
# Julian Aparicio
# japaric4@uci.edu
# 74237345

import urllib
import json
from urllib import request, error
from abc import ABC, abstractmethod


class HttppError(Exception):
    '''
    This class catches HTTP errors in my code.
    '''
    def __init__(self, msg):
        self.msg_http = msg
        print(self.msg_http)


class FourfourError(Exception):
    '''
    This exception class is raised when a 404 error occurs
    '''
    def __init__(self, msg):
        self.msg_fouro = msg
        print(self.msg_fouro)


class FiveoError(Exception):
    '''
    This exception class is raised when a 503 error occurs
    '''
    def __init__(self, msg):
        self.msg_fiveo = msg
        print(self.msg_fiveo)


class InvdFrmt(Exception):
    '''
    This exception class is raised when an invalid format error occurs
    '''
    def __init__(self, msg):
        self.msg_invld = msg
        print(self.msg_invld)


class LossConn(Exception):
    '''
    This exception class is raised when a loss of connection error occurs
    '''
    def __init__(self, msg):
        self.msg_loss_cnnt = msg
        print(self.msg_loss_cnnt)


class FouroneError(Exception):
    '''
    This exception class is raised when a 401 error occurs
    '''
    def __init__(self, msg):
        self.msg_four_none = msg
        print(self.msg_four_none)


class WebAPI(ABC):
    '''
    The WebAPI class is the base class for the OpenWeather and
     LastFM api modules. It's main purpose is it's _download_url
     method. It also enforces two abstract classes on its child classes.
    '''
    def _download_url(self, url: str) -> dict:
        '''
        The _download_url method is special because it is called from
        the OpenWeather and LastFM modules. Since both modules have an
        identical _download_url method, it made sense to short the code
        in both modules and put it all into a base class. Which is done
        here. All errors that could happen with the api are also covered
        in this method. The r_obj variable is returned and contains the
        json object which all data from the api is pulled from.
        '''
        response = None
        r_obj = None
        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)
        except urllib.error.HTTPError as exc4:
            if exc4.code == 403:
                print('Failed to donwload contents of URL')
                print(f"Status code {exc4.code}")
                raise HttppError("Your API key is wrong.") from exc4
            if exc4.code == 401:
                print('Failed to donwload contents of URL')
                print(f"Status code {exc4.code}")
                raise FouroneError("Your API key is wrong.") from exc4
                return None
            if exc4.code == 404:
                print('Server error.')
                print(f"Status code {exc4.code}")
                raise FourfourError("Server error.") from exc4
            if exc4.code == 503:
                print('Server is unavailable to handle incoming requests.')
                print(f"Status code {exc4.code}")
                raise FiveoError("Server down right now.") from exc4
        except TypeError as exc2:
            raise InvdFrmt("API data returned in wrong format.") from exc2
        except urllib.error.URLError as exc:
            raise LossConn("Loss of local connection to internet.") from exc
        finally:
            if response is not None:
                response.close()
            return r_obj

    def set_apikey(self, apikey: str) -> None:
        '''
        This is the set_apikey which is used in the child classes.
        '''
        pass

    @abstractmethod
    def load_data(self):
        '''
        This is an abstract method, so it's ensuring that all
         child classes must have the load_data method in them.
         '''
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        '''
        This is an abstract method, so it's ensuring that all
         child classes must have the transclude method in them.
        '''
        pass
