from dji_drone import DjiDrone
from drone_adapter import DroneAdapter
from wild_turky import WildTurky
from turky_adapter import TurkyAdapter
from mallard_duck import MallardDuck


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    drone = DjiDrone()
    droneAdapter = DroneAdapter(drone)
    test_duck(droneAdapter)
    turky = WildTurky()
    turkyAdapter = TurkyAdapter(turky)
    test_duck(turkyAdapter)
    m_duck = MallardDuck()
    test_duck(m_duck)
