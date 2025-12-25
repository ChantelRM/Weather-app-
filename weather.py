import requests
import math

# TODO:
    # - Add the get condition,weather key, descption key
    # - advice for weather conditions based on temp max and temp min in main key dict[nested] and the weather description key in weather dict in list
    # -add error handlin gfor if data is not found for temp
    # -change return for temp function, maybe have get temp min and temp max functions
    # - Add wind speed, direction

class Weather:
    def __init__(self,city):
        self.city = city
        self.api_key = '5c940fbc1f7fa426e6c24c05fd945af8'
        self.data = None
        self.get_condition()
        self.get_current_temp()
        self.advice()
        self.get_feels()
        self.get_humidity()
        self.get_temp_max()
        self.get_temp_min()

    #  key = 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
    # key 5c940fbc1f7fa426e6c24c05fd945af8

    def fetch_data(self):
        '''
        This function gets data about the city's weather from the OpenWeather api
        uses api key and city to get data, get the url needed for requests
        '''

        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric'
    
        
        # send a get request to url
        try:
            response = requests.get(url) #converting to json allows us to access individual attributes
            self.data =response.json()
            # for key,value in self.data.items():
            #     print(key,value)
            # print(self.data)
            # return self.data
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data {e}')


    def get_current_temp(self):  
        return self.data['main']['temp']
    
    def get_feels(self):
        return self.data['main']['feels_like']
    
    def get_temp_max(self):
        '''
        Docstring for get_temp
        This function fetches the temperature of he entered city from the api
        :param self: Description
        '''
        return self.data['main']['temp_max']

    def get_temp_min(self):
        return self.data['main']['temp_min']
    
    def get_humidity(self):
        return self.data['main']['humidity']

    def get_condition(self):
        '''
        Docstring for get_condition
        This function gets the city weather rcondition eg. rainy, cloudy, windy, showers etc.

        :param self: Description
        '''
        return self.data['weather'][0]['description']

    def advice(self):
        '''
        Docstring for advice
        Based on the condition, this fuction returns basic advice to the user based on the weather condition

        :param self: Description
        '''

        WEATHER_EMOJIS = {
                        "clear sky": "☀️",
                        "few clouds": "🌤️",
                        "scattered clouds": "⛅",
                        "partially cloudy": '\u2601',
                        "broken clouds": "☁️",
                        "shower rain": "🌦️",
                        "rain": "🌧️",
                        'shower': '\u2614',
                        "thunderstorm": "⛈️",
                        "snow": "❄️",
                        "mist": "🌫️"
                    }
    
        if 'sunny' or 'clear' in self.get_condition():
            ...
    pass


city = input('City,Country:     ')
# weather = Weather(city,api_key = '5c940fbc1f7fa426e6c24c05fd945af8')
weather = Weather(city)
weather.fetch_data()
# print(weather.get_temp())