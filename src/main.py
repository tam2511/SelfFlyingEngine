from src import Quadcopter, Session, Control


if __name__ == '__main__':
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session, autopilot=True)
