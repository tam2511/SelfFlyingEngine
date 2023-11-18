from master.src.quadcopter import Quadcopter
from master.src.core import Core


if __name__ == '__main__':
    drone = Quadcopter('Tello', ip='0.0.0.0')
    core = Core(drone)
