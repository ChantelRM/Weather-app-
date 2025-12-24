import requests
import math

# TODO:
# - Add the get condition,weather key, descption key
# - advice for weather conditions based on temp max and temp min in main key dict[nested] and the weather description key in weather dict in list
# -add error handlin gfor if data is not found for temp
# -change return for temp function, maybe have get temp min and temp max functions
class Weather:
    def __init__(self,city,api_key):
        self.city = city
        self.api_key = api_key
        self.data = None
    #  key = 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
    # key 5c940fbc1f7fa426e6c24c05fd945af8

    def fetch_data(self):
        '''
        Docstring for fetch_data
        This function gets data about the city's weather from the OpenWeather api
        uses api key and city to get data, get the url needed for requests
        
        :param self: Description
        '''

        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric'
        # url= f'https://api.openweathermap.org/data/2.5/weather?lat={self.city}&lon={self.city}&appid={self.api_key}'
        
        # send a get request to url
        try:
            response = requests.get(url) #converting to json allows us to access individual attributes
            self.data =response.json()
            for key,value in self.data.items():
                print(key,value)
            # print(self.data)
            # return self.data
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data {e}')

    def get_temp(self):
        '''
        Docstring for get_temp
        This function fetches the temperature of he entered city from the api
        :param self: Description
        '''
        return self.data['main']

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


city = input('City,Country:     ')
weather = Weather(city,api_key = '5c940fbc1f7fa426e6c24c05fd945af8')
weather.fetch_data()
print(weather.get_temp())