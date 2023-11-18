import cv2
from .base import BaseFrame


class VideoStream(BaseFrame):
    def __init__(self, window_name):
        super().__init__()
        self.window_name = window_name

    def processing(self):
        cv2.startWindowThread()

        while self.is_alive:
            frame = self.frames.get()
            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
            cv2.imshow(self.window_name, frame)
            cv2.resizeWindow(self.window_name, frame.shape[1], frame.shape[0])

        cv2.destroyAllWindows()
