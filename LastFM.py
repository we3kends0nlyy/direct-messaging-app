'''
The LastFM module is used for the LastFM api. It has several
methods which take the data considering the artist that has either been chosen
by the user or defaultly set if they don't choose their own artist.
'''
# Julian Aparicio
# japaric4@uci.edu
# 74237345
from WebAPI import WebAPI


class LastFM(WebAPI):
    '''
    This class is for the LastFM api and instantiates an the
    artist in the init. This class is
    a child class of the WebAPI base class.
    '''

    def __init__(self, artist="Drake"):
        super().__init__()
        self.artist = artist
        self.apikey = None

    def set_apikey(self, apikey: str) -> None:
        '''
        This method sets the api key for the LastFM module.
        '''
        self.apikey = apikey

    def load_data(self) -> None:
        '''
        The load_data method calls the _download_url
         method from the base class WebAPI. This method also assigns data from
         the LastFM api to class variables
         which are used in the tran_iden method.
        '''
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.get\
info&artist={self.artist}&api_key={self.apikey}&format=json"
        fm_ob_artist = super()._download_url(url)
        if fm_ob_artist is not None:
            artist = self.artist
            LastFM.artist_spaces = artist.replace("+", " ")
            try:
                LastFM.listeners = fm_ob_artist['artist']['stats']['listeners']
                LastFM.genre = fm_ob_artist['artist']['tags']['tag'][0]['name']
                return True
            except KeyError:
                print("ERROR")
                print("Invalid artist.")
        else:
            return None

    def tran_iden(self, keyword):
        '''
        The tran_iden method is called from the transclude
        method and check what keywords are present.
        If a certain piece of data equals a
        certain keyword, then that piece of data is returned and
        sent to be replaced in the transclude method.
        '''
        try:
            if keyword == "@lastfm":
                return LastFM.genre
            if keyword == "@artist":
                return LastFM.artist_spaces
            if keyword == "@artistlisteners":
                return LastFM.listeners
        except AttributeError:
            pass
        except IndexError:
            print("ERROR")
            print("Invalid artist.")

    def transclude(self, message: str) -> str:
        '''
        The transclude function checks which keywords are in the message.
        If a keyword is found in the message,
        the keyword is sent to the tran_iden method.
        '''
        lst_of_keywords = ["@lastfm", "@artistlisteners", "@artist"]
        for i in lst_of_keywords:
            if i in message:
                data = self.tran_iden(i)
                message = message.replace(i, str(data))
        return message
