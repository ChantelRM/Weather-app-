import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv('weather_api_key')
if not api_key:
    raise ValueError("api key not found. check .env")

# TODO:
    # - advice for weather conditions based on temp max and temp min 


class Weather:
    def __init__(self,city):
        self.city = city
        self.api_key = api_key
        self.data = None

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
    
    def get_wind_direction(self):
        degree = self.data['wind']['deg']
        if degree == None:
            return None
        
        if 337.5 <= degree <= 22.5:
            return 'N'
        elif 22.5 <= degree <= 67.5:
            return 'NE'
        elif 67.5 <= degree <= 112.5:
            return 'E'
        elif 112.5 <= degree <= 157.5:
            return 'SE'
        elif 157.5 <= degree <= 202.5:
            return 'S'
        elif 202.5 <= degree <= 247.5:
            return 'SW'
        elif 247.5 <= degree <= 292.5:
            return 'W'
        elif 292.5 <= degree <= 337.5:
            return 'NW'   
    
    def get_wind_speed(self):
        if not self.data:
            return None
        return self.data['wind']['speed']

    def advice(self):
        '''
        Based on the condition, this fuction returns basic advice to the user based on the weather condition
        '''
        condition = self.get_condition()
    
        if not condition:
            return 'No data availible'
        elif 'sun' in condition or 'clear' in condition:
            return "Clear skies! ☀️"
        elif 'shower' in condition or 'rain' in condition or 'thunder' in condition:
            return "Uhm...you should take an umbrella! 🌧️"
        elif 'snow' in condition:
            return "Dress warm! ❄️"
        elif 'fog' in condition or 'mist' in condition :
            return "Visibilty is not great stay cautious while driving! 🌫️"
        elif 'cloud' in condition:
            return "Mmm... A bit cloudy... ☁️"
        else:
            return 'Mmm, seem slike a normal day'

def main():
    city = input('Enter city -> ')
    weather = Weather(city)
    weather.fetch_data()
    print(f'Condition:  {weather.get_condition()}')
    print(f'Current temperature: {weather.get_current_temp():.0f}°C')
    print(f'Feels like: {weather.get_feels():.0f}°C')
    print(f'Max. temperature: {weather.get_temp_max():.0f}°C')
    print(f'Min. temperature: {weather.get_temp_min():.0f}°C')
    print(f'Speed: {weather.get_wind_speed()}km/h, Direction: {weather.get_wind_direction()}')
    print(f'Humidity: {weather.get_humidity()}%')
    print(f'Advice: {weather.advice()}')

if __name__=='__main__':
    main()