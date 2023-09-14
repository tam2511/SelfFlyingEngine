from src import Quadcopter, Session, Control, Simulator


if __name__ == '__main__':
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session, autopilot=True)
        Simulator(control, distance=10, degree=10)
