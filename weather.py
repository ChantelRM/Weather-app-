import requests
import math


class Weather:
    def __init__(self,city,api_key,data = None):
        self.city = city
        self.api_key = api_key
        self.data = data
    #  key = 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
    # key 5c940fbc1f7fa426e6c24c05fd945af8

    def fetch_data(self,city,api):
        '''
        Docstring for fetch_data
        This function gets data about the city's weather from the OpenWeather api
        uses api key and city to get data, get the url needed for requests
        
        :param self: Description
        '''
        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        # url= f'https://api.openweathermap.org/data/2.5/weather?lat={self.city}&lon={self.city}&appid={self.api_key}'
        
        # send a get request to url
        response = requests.get(url).json() #converting to json allows us to access individual attributes
        if response.status_code == 200:
            return response
        else :
            print(f'Error {response.status_code} - {response.text}')
    def get_temp(self):
        '''
        Docstring for get_temp
        This function fetches the temperature of he entered city from the api
        :param self: Description
        '''
        pass

    def get_condition(self):
        '''
        Docstring for get_condition
        This function gets the city weather rcondition eg. rainy, cloudy, windy, showers etc.

        :param self: Description
        '''
        pass

    def advice(self):
        '''
        Docstring for advice
        Based on the condition, this fuction returns basic advice to the user based on the weather condition

        :param self: Description
        '''
        pass

weather = Weather()
city = input('City,Country')
weather.fetch_data()