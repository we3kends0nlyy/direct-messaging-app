'''
The OpenWeather module is used for the OpenWeather api.
It has several methods including transclude which takes a message from the
user and transclude the message with keywords
that were specified in the message.
'''
# Julian Aparicio
# japaric4@uci.edu
# 74237345
from datetime import datetime
from WebAPI import WebAPI


class OpenWeather(WebAPI):
    '''
    This class is for the OpenWeather api and
    instantiates the user zip code and country code.
    '''

    def __init__(self, zip_code="92697", ccode="US"):
        super().__init__()
        if zip_code is None:
            self.zip = "92697"
        else:
            self.zip = zip_code
        if ccode is None:
            self.ccode = "US"
        else:
            self.ccode = ccode
        self.apikey = None

    def set_apikey(self, apikey: str) -> None:
        '''
        This method sets my api key for the OpenWeather module.
        '''
        self.apikey = apikey

    def load_data(self) -> None:
        '''
        The load_data method calls the _download_url
         method from the base class WebAPI.
        This method also assigns data from the OpenWeather api to
        class variables which are used in the tran_iden method.
        '''
        url = f"http://api.openweathermap.org/data/2.5/weath\
er?zip={self.zip},{self.ccode}&appid={self.apikey}"
        weather_obj = super()._download_url(url)
        if weather_obj is not None:
            OpenWeather.temperature = weather_obj['main']['temp']
            OpenWeather.low_temperature = weather_obj['main']['temp_min']
            OpenWeather.description = weather_obj['weather'][0]['description']
            OpenWeather.sunset = weather_obj['sys']['sunset']
            return True
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
            if keyword == "@weather":
                return OpenWeather.description
            if keyword == "@temp":
                real_temp = float(OpenWeather.temperature)
                real_temp2 = ((real_temp - 273.15) * (9/5)) + 32
                temp_round = round(real_temp2, 2)
                temp_final = str(temp_round) + " Degrees"
                return temp_final
            if keyword == "@lowtemp":
                real_temp = float(OpenWeather.low_temperature)
                real_temp2 = ((real_temp - 273.15) * (9/5)) + 32
                temp_round = round(real_temp2, 2)
                temp_final3 = str(temp_round) + " Degrees"
                return temp_final3
            if keyword == "@sunset":
                real_time = datetime.fromtimestamp(int(OpenWeather.sunset))
                time_string = str(real_time)
                time_split = time_string.split(" ")
                return time_split[-1]
        except AttributeError:
            pass

    def transclude(self, message: str) -> str:
        '''
        The transclude function checks which keywords
        are in the message.
        If a keyword is found in the message, the keyword
        is sent to the tran_iden method.
        '''
        lst_of_keywords = ["@weather", "@temp", "@lowtemp",  "@sunset"]
        for i in lst_of_keywords:
            if i in message:
                data = self.tran_iden(i)
                message = message.replace(i, str(data))
        return message
