from abc import ABC, abstractmethod


class InterfaceConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
