from abc import ABC, abstractmethod
import tkinter
from datetime import datetime
from time import *
from tkinter import scrolledtext
import pytz as pytz
from login import login
import requests

#the abstract methods are because at fist it was built like a game and it had different players
class Player(ABC):

    def __init__(self):
        pass

    Birthday = False
    sent_message = False
    Hungry = False
    Tired = False

    @abstractmethod
    def is_tired(self):
        pass

    @abstractmethod
    def is_hungry(self):
        pass


class TkinterTerminal:
    def __init__(self, master, width=1400, height=5):
        self.width = width
        self.height = height
        self.text_widget = scrolledtext.ScrolledText(master, wrap=tkinter.WORD, width=self.width, height=self.height)
        self.text_widget.pack(side=tkinter.BOTTOM)

    def write(self, message):
        self.text_widget.insert(tkinter.END, message)
        self.text_widget.see(tkinter.END)



class WeatherWidget:
    def __init__(self, master):
        self.wwidget_frame = tkinter.Frame(master, width=10, height=10)
        self.wwidget_frame.place(x=0, y=528)
        self.conditions_label = tkinter.Label(self.wwidget_frame,
                                        font="Arial",
                                        width=18)
        self.conditions_label.config(relief=tkinter.SUNKEN)
        self.conditions_label.pack()
        self.temp_label = tkinter.Label(self.wwidget_frame,
                                       font="Arial",
                                       width=18)
        self.temp_label.config(relief=tkinter.SUNKEN)
        self.temp_label.pack()
        self.wind_label = tkinter.Label(self.wwidget_frame,
                                        font="Arial",
                                        width=18)
        self.wind_label.config(relief=tkinter.SUNKEN)
        self.wind_label.pack()

        self.api_key = '376865cfd8b0401e3523f32a0065c8f7'
        self.city = 'Barcelona'
        self.sunset_time = None
        self.update_weather_labels()

    def get_weather(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': self.city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        conditions = data['weather'][0]['description']
        temp_current = round(data['main']['temp'])
        temp_max = round(data['main']['temp_max'])
        temp_min = round(data['main']['temp_min'])
        wind_speed = round(data['wind']['speed'])

        sunset_timestamp = data['sys']['sunset']
        sunset_utc_time = datetime.utcfromtimestamp(sunset_timestamp)
        local_timezone = pytz.timezone('Europe/Madrid')
        sunset_local_time = sunset_utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
        self.sunset_time = sunset_local_time.strftime('%H:%M')

        return conditions, temp_current, temp_max, temp_min, wind_speed

    def update_weather_labels(self):
        conditions, temp_current, temp_max, temp_min, wind_speed = self.get_weather()
        self.conditions_label.config(text=f"{conditions.capitalize()}")
        self.temp_label.config(text=f"{temp_current}°C |({temp_min}°C - {temp_max}°C)")
        self.wind_label.config(text=f"Вятър: {wind_speed} m/s")
        self.wwidget_frame.after(3600000, self.update_weather_labels)



class TimeKeeping:
    def __init__(self, master):
        self.clock_frame = tkinter.Frame(master, width=10, height=10)
        self.clock_frame.place(x=0, y=0)
        self.time_label = tkinter.Label(self.clock_frame,
                                        font="Arial",
                                        width=25)
        self.time_label.config(relief=tkinter.SUNKEN)
        self.time_label.pack()
        self.day_label = tkinter.Label(self.clock_frame,
                                       font="Arial",
                                       width=25)
        self.day_label.config(relief=tkinter.SUNKEN)
        self.day_label.pack()
        self.date_label = tkinter.Label(self.clock_frame,
                                        font="Arial",
                                        width=25)
        self.date_label.config(relief=tkinter.SUNKEN)
        self.date_label.pack()
        self.update_time()

    def update_time(self):
        self.time_string = strftime("%I:%M:%S %p")
        self.time_label.config(text=self.time_string)

        self.day_string = strftime("%A")
        self.day_label.config(text=self.day_string)

        self.date_string = strftime("%B %d, %Y")
        self.date_label.config(text=self.date_string)
        self.date_checker = strftime("%B %d")
        if self.date_checker == login.User1.Birthdate:
            login.User1.Birthday = True
        else:
            login.User1.Birthday = False

        self.time_label.after(200, self.update_time)