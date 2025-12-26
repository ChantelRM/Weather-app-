import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv('api_key')

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
        # self.get_condition()
        # self.get_current_temp()
        # self.advice()
        # self.get_feels()
        # self.get_humidity()
        # self.get_temp_max()
        # self.get_temp_min()

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
            response.raise_for_status()
            self.data =response.json()
            # for key,value in self.data.items():
            #     print(key,value)
            # print(self.data)
            return True
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data {e}')
            return False

    def get_current_temp(self):  
        if not self.data:
            return None
        return self.data['main']['temp']
    
    def get_feels(self):
        if not self.data:
            return None
        return self.data['main']['feels_like']
    
    def get_temp_max(self):
        if not self.data:
            return None
        return self.data['main']['temp_max']

    def get_temp_min(self):
        if not self.data:
            return None
        return self.data['main']['temp_min']
    
    def get_humidity(self):
        if not self.data:
            return None
        return self.data['main']['humidity']

    def get_condition(self):
        if not self.data:
            return None
        return self.data['weather'][0]['description']

    def advice(self):
        '''
        Based on the condition, this fuction returns basic advice to the user based on the weather condition
        '''
        condition = self.get_condition().lower()

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
    
        if 'sunny' or 'clear' in condition:
            ...
        elif 'shower':

        elif 'rain':

        elif 'thunder':

        elif 'snow':

        elif 'fog' or 'mist' :

        elif 'scattered clouds' or 'partially cloud':
    pass

def main():

    city = input('City:     ')
    # weather = Weather(city,api_key = '5c940fbc1f7fa426e6c24c05fd945af8')
    weather = Weather(city)
    weather.fetch_data()
    print(f'Condition:  {weather.get_condition()}')
    print(f'Current temperature: {weather.get_current_temp():.0f}°C')
    print(f'Feels like: {weather.get_feels():.0f}°C')
    print(f'Max. temperature: {weather.get_temp_max():.0f}°C')
    print(f'Min. temperature: {weather.get_temp_min():.0f}°C')

if __name__=='__main__':
    main()