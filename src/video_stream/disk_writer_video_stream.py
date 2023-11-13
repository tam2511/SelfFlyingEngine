import cv2
import numpy as np

from queue import Queue
from threading import Thread


class DiskWriterVideoStream(object):
    __AVAILABLE_FORMATS = ('avi',)

    def __new__(
            cls,
            rec_path: str,
            width: int,
            height: int,
            fps: int
    ):
        rec_format = rec_path.split('.')[-1]

        if rec_format not in cls.__AVAILABLE_FORMATS:
            raise NameError(f'«{rec_format}» format is not available')

        return object.__new__(cls)

    def __init__(
            self,
            rec_path: str,
            width: int,
            height: int,
            fps: int
    ):
        self.__writer = cv2.VideoWriter(rec_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
        self.__queue = Queue()

        Thread(target=self.__write).start()

    def put(self, frame: np.ndarray | bool):
        if not isinstance(frame, np.ndarray | bool):
            raise TypeError(f'{type(frame)} is not {np.ndarray} or {bool}')

        self.__queue.put(frame)

    def __write(self):
        while True:
            frame = self.__queue.get()
            if frame is False:
                break
            self.__writer.write(frame)

        self.__writer.release()
