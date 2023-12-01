from djitellopy import Tello
from .base import BaseAPI


class TelloAPI(BaseAPI):
    def __init__(self, ip: str):
        self.api = Tello(host=ip)

    def connect(self):
        # self.api.connect()
        ...

    def disconnect(self):
        self.api.end()

    def get_frame_read(self):
        return self.api.get_frame_read()

    def takeoff(self):
        self.api.takeoff()

    def land(self):
        self.api.land()

    def up(self, distance: int):
        self.api.move_up(distance)

    def down(self, distance: int):
        self.api.move_down(distance)

    def left(self, distance: int):
        self.api.move_left(distance)

    def right(self, distance: int):
        self.api.move_right(distance)

    def forward(self, distance: int):
        self.api.move_forward(distance)

    def back(self, distance: int):
        self.api.move_back(distance)

    def clockwise(self, degree: int):
        self.api.rotate_clockwise(degree)

    def counter_clockwise(self, degree: int):
        self.api.rotate_counter_clockwise(degree)
