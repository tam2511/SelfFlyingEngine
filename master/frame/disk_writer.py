import cv2
from .base import BaseFrame


class DiskWriter(BaseFrame):
    def __init__(self, path, width=400, height=300, fps=30):
        super().__init__()
        self.disk_writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    def processing(self):
        while self.is_alive:
            frame = self.frames.get()
            self.disk_writer.write(frame)

        self.disk_writer.release()
