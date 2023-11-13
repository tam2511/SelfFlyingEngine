from src import Quadcopter, Session, Control
from src.video_stream import DiskWriterVideoStream, RealTimeVideoStream


if __name__ == '__main__':
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session, autopilot=True)
        disk_writer = DiskWriterVideoStream('tello.avi', 400, 300, 30)
        RealTimeVideoStream(session, disk_writer)
