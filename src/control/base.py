from src.interfaces import InterfaceAction
from src.decorators import decorating_all_public_methods, ignored_method, available_method
from src import Session
from src.exceptions import UsageError


@decorating_all_public_methods(ignored_method, available_method)
class Control(InterfaceAction):
    __USED_SESSIONS = []

    def __new__(
            cls,
            session: Session,
            autopilot: bool = False
    ):
        if not isinstance(session, Session):
            raise TypeError(f'{type(session)} is not {Session}')

        cls.__check_autopilot_type(autopilot)

        if session in cls.__USED_SESSIONS:
            raise UsageError(f'{session} is already under control')

        cls.__USED_SESSIONS.append(session)

        return object.__new__(cls)

    def __init__(
            self,
            session: Session,
            autopilot: bool = False
    ):
        self.__model = session.quadcopter.model
        self.__session = session
        self.__autopilot = autopilot

    @property
    def access(self):
        return self.__session.active

    @property
    def autopilot(self):
        return self.__autopilot

    @autopilot.setter
    def autopilot(self, value: bool):
        self.__check_autopilot_type(value)
        self.__autopilot = value

    @staticmethod
    def __check_autopilot_type(autopilot: bool):
        if not isinstance(autopilot, bool):
            raise TypeError(f'{type(autopilot)} is not {bool}')

    def execute(
            self,
            method_name: str,
            *args
    ):
        if (
            method_name in ('connect', 'disconnect')
            or not hasattr(self.__model, method_name)
        ):
            raise NameError(f'{self} cannot execute method «{method_name}»')

        getattr(self.__model, method_name).__call__(*args)

    def takeoff(self):
        self.__model.takeoff()

    def land(self):
        self.__model.land()

    def up(self, distance: int):
        self.__model.up(distance)

    def down(self, distance: int):
        self.__model.down(distance)

    def left(self, distance: int):
        self.__model.left(distance)

    def right(self, distance: int):
        self.__model.right(distance)

    def forward(self, distance: int):
        self.__model.forward(distance)

    def back(self, distance: int):
        self.__model.back(distance)

    def clockwise(self, degree: int):
        self.__model.clockwise(degree)

    def counter_clockwise(self, degree: int):
        self.__model.counter_clockwise(degree)
