from observer import Observer
from display import Display


class UserDisplay(Observer, Display):
    def __init__(self, weather_station):
        self.__humidity = None
        self.__temp = None
        self.__pressure = None
        self.__weather_station = weather_station
        self.__weather_station.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.__humidity = humidity
        self.__temp = temp
        self.__pressure = pressure
        self.display()

    def display(self):
        print(f'{self.__temp} {self.__pressure} {self.__humidity}')
