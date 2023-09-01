from abc import ABC, abstractmethod


class InterfaceAction(ABC):
    @abstractmethod
    def takeoff(self):
        pass

    @abstractmethod
    def land(self):
        pass

    @abstractmethod
    def up(self, distance: int):
        pass

    @abstractmethod
    def down(self, distance: int):
        pass

    @abstractmethod
    def left(self, distance: int):
        pass

    @abstractmethod
    def right(self, distance: int):
        pass

    @abstractmethod
    def forward(self, distance: int):
        pass

    @abstractmethod
    def back(self, distance: int):
        pass

    @abstractmethod
    def clockwise(self, degree: int):
        pass

    @abstractmethod
    def counter_clockwise(self, degree: int):
        pass
