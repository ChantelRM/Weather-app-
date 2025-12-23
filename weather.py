class Weather:
    def __init__(self,city,api_key,data=None):
        self.city = city
        self.api_key = api_key
        self.data = data
    
    def fetch_data(self):
        '''
        Docstring for fetch_data
        This function gets data about the city's weather from the OpenWeather api
        
        :param self: Description
        '''
        pass

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