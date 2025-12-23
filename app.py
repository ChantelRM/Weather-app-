import tkinter as tk
import Weather 

class WeatherApp:
    def __init__(self):
        self.window = tk.Tk()
        self.history =[]

    def run(self):
        '''
        Docstring for run
        This function runs the weather app and displays the window, labels
        :param self: Description
        '''
        self.window.mainloop()

    def search_city(self):
        '''
        Docstring for search_city
        THis is the main logic for the app. 
        We get input from the user, the city. Based on the city we return the weather temperature, condtion and advice to the user along with the advice
        :param self: Description
        '''
        # read city from widget
        # create weather instance
        # call fetch
        # update the weather labels, give advice
        # store search history
        
        pass

if '__name__' == '__main__':
    city = input('Search city')
    weather = Weather()
 
