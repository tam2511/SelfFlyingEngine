from djitellopy import Tello
from src.interfaces import InterfaceConnection, InterfaceAction


class TelloAPI(InterfaceConnection, InterfaceAction):
    def __init__(self, ip: str):
        self.__api = Tello(host=ip)

    def connect(self):
        self.__api.connect()

    def disconnect(self):
        self.__api.end()

    def takeoff(self):
        self.__api.takeoff()

    def land(self):
        self.__api.land()

    def up(self, distance: int):
        self.__api.move_up(distance)

    def down(self, distance: int):
        self.__api.move_down(distance)

    def left(self, distance: int):
        self.__api.move_left(distance)

    def right(self, distance: int):
        self.__api.move_right(distance)

    def forward(self, distance: int):
        self.__api.move_forward(distance)

    def back(self, distance: int):
        self.__api.move_back(distance)

    def clockwise(self, degree: int):
        self.__api.rotate_clockwise(degree)

    def counter_clockwise(self, degree: int):
        self.__api.rotate_counter_clockwise(degree)
