from weather_station import WeatherStation
from tempreture import Tempreture
from user_display import UserDisplay

if __name__ == '__main__':
    data = WeatherStation()

    tempDisplay = Tempreture(data)
    show = UserDisplay(data)
    data.set_value(10, 1, 5)
