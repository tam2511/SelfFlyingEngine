from src import Quadcopter


class Session(object):
    __ACTIVE_SESSIONS = {}

    def __new__(
            cls,
            quadcopter: Quadcopter
    ):
        if quadcopter in cls.__ACTIVE_SESSIONS:
            raise RuntimeError(f'{quadcopter} is already in session')

        cls.__start(quadcopter)

        return object.__new__(cls)

    def __init__(
            self,
            quadcopter: Quadcopter
    ):
        self.__quadcopter = quadcopter
        self.__class__.__ACTIVE_SESSIONS[quadcopter] = self

    @property
    def quadcopter(self):
        return self.__quadcopter

    @property
    def active(self):
        return self in self.__ACTIVE_SESSIONS.values()

    @staticmethod
    def __start(quadcopter: Quadcopter):
        try:
            # quadcopter.model.connect()
            ...
        except Exception:
            raise ConnectionError(f'{quadcopter} is not available')

    def finish(self):
        if self.active:
            self.__quadcopter.model.disconnect()
            del self.__class__.__ACTIVE_SESSIONS[self.__quadcopter]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()
