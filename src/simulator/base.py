from pynput.keyboard import Listener, Key, KeyCode
from src import Control


class Simulator(object):
    def __new__(
            cls,
            control: Control,
            **kwargs
    ):
        if not isinstance(control, Control):
            raise TypeError(f'{type(control)} is not {Control}')

        return object.__new__(cls)

    def __init__(
            self,
            control: Control,
            *,
            distance: int = 1,
            degree: int = 1
    ):
        self.__control = control
        self.__distance = distance
        self.__degree = degree
        self.__run()

    def __run(self):
        listener = Listener(on_release=self.__press, suppress=True)
        listener.start()
        listener.join()

    def __press(
            self,
            key: Key | KeyCode
    ):
        match key:
            case Key.esc:
                return False

            case Key.space:
                self.__control.autopilot = not self.__control.autopilot
                print(f'{self.__control} autopilot position «{self.__control.autopilot}»')

            case Key.enter:
                self.__control.takeoff()

            case Key.backspace:
                self.__control.land()

            case Key.up:
                self.__control.up(self.__distance)

            case Key.down:
                self.__control.down(self.__distance)

            case Key.right:
                self.__control.clockwise(self.__degree)

            case Key.left:
                self.__control.counter_clockwise(self.__degree)

            case KeyCode(char='w'):
                self.__control.forward(self.__distance)

            case KeyCode(char='s'):
                self.__control.back(self.__distance)

            case KeyCode(char='a'):
                self.__control.left(self.__distance)

            case KeyCode(char='d'):
                self.__control.right(self.__distance)
