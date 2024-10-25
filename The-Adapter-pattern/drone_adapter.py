from duck import Duck


class DroneAdapter(Duck):

    def __init__(self, drone):
        self.__drone = drone

    def fly(self):
        self.__drone.spin_rotors()
        self.__drone.take_off()

    def quack(self):
        self.__drone.beep()
