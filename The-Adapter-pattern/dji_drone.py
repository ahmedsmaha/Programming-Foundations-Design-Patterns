from drone import Drone


class DjiDrone(Drone):

    def beep(self):
        print("Beep beep beep")

    def spin_rotors(self):
        print("Rotors are spinning")

    def take_off(self):
        print("Taking off")
