from observer import Observer
from display import Display


class Tempreture(Observer, Display):
    def __init__(self, weather_station):
        self.__weather_station = weather_station
        self.__weather_station.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.display()

    def display(self):
        print("Improving weather on the way!")
