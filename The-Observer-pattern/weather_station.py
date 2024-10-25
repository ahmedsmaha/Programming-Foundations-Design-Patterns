from subject import Subject


class WeatherStation(Subject):
    def __init__(self):
        self.__temp = None
        self.__humidity = None
        self.__pressure = None
        self.__observers = []

    def register_observer(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove_observer(self, observer):
        try:
            self.__observers.remove(observer)
        except ValueError:
            pass

    def notify_observer(self):
        for observer in self.__observers:
            observer.update(self.__temp, self.__humidity, self.__pressure)

    def set_value(self, temp, humidity, pressure):
        self.__temp = temp
        self.__humidity = humidity
        self.__pressure = pressure
        self.notify_observer()
