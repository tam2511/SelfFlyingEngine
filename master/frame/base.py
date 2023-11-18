from abc import ABC, abstractmethod
from threading import Thread
from queue import Queue


class BaseFrame(ABC):
    def __init__(self):
        self.frames = Queue()
        self.is_alive = True
        Thread(target=self.processing).start()

    def put(self, frame):
        self.frames.put(frame)

    def stop(self):
        self.is_alive = False

    @abstractmethod
    def processing(self):
        pass
