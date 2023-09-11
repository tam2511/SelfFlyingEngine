from src import Quadcopter, Session


if __name__ == '__main__':
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        pass
