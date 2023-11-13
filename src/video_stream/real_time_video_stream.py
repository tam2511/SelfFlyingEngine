import cv2

from src import Session
from src.video_stream import DiskWriterVideoStream
from src.exceptions import UsageError
from threading import Thread


class RealTimeVideoStream(object):
    __USED_SESSIONS = []

    def __new__(
            cls,
            session: Session,
            disk_writer: DiskWriterVideoStream | None = None
    ):
        if not isinstance(session, Session):
            raise TypeError(f'{type(session)} is not {Session}')

        if session in cls.__USED_SESSIONS:
            raise UsageError(f'Stream for the {session} has already been created')

        cls.__USED_SESSIONS.append(session)

        return object.__new__(cls)

    def __init__(
            self,
            session: Session,
            disk_recorder: DiskWriterVideoStream | None = None
    ):
        self.__model = session.quadcopter.model
        self.__session = session
        self.__disk_recorder = disk_recorder
        self.__video_capture = self.__model.get_frame_read()

        Thread(target=self.__video_stream).start()

    def __video_stream(self):
        self.__model.streamon()
        window_name = self.__model.__class__.__name__
        cv2.startWindowThread()

        while self.__session.active:
            frame = self.__video_capture.frame

            if self.__disk_recorder:
                self.__disk_recorder.put(frame)

            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.imshow(window_name, frame)
            cv2.resizeWindow(window_name, frame.shape[1], frame.shape[0])

        if self.__disk_recorder:
            self.__disk_recorder.put(False)

        cv2.destroyAllWindows()
        self.__model.streamoff()
