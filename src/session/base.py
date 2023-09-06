from src import Quadcopter
from src.exceptions import UsageError


class Session(object):
    __USED_QUADCOPTERS = []
    __ACTIVE_SESSIONS = []

    def __new__(
            cls,
            quadcopter: Quadcopter
    ):
        if not isinstance(quadcopter, Quadcopter):
            raise ValueError(f'{type(quadcopter)} is not {Quadcopter}')

        if quadcopter in cls.__USED_QUADCOPTERS:
            raise UsageError(f'{quadcopter} is already in session')

        cls.__start(quadcopter)

        return object.__new__(cls)

    def __init__(
            self,
            quadcopter: Quadcopter
    ):
        self.__quadcopter = quadcopter
        self.__class__.__USED_QUADCOPTERS.append(quadcopter)
        self.__class__.__ACTIVE_SESSIONS.append(self)

    @property
    def quadcopter(self):
        return self.__quadcopter

    @property
    def active(self):
        return self in self.__ACTIVE_SESSIONS

    @staticmethod
    def __start(quadcopter: Quadcopter):
        try:
            quadcopter.model.connect()
        except Exception:
            raise ConnectionError(f'{quadcopter} is not available')

    def finish(self):
        if self.active:
            self.__quadcopter.model.disconnect()
            self.__class__.__USED_QUADCOPTERS.remove(self.__quadcopter)
            self.__class__.__ACTIVE_SESSIONS.remove(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()
