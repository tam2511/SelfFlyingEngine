from src.api import TelloAPI


class Quadcopter(object):
    __AVAILABLE_MODELS = {
        'Tello': TelloAPI
    }

    def __new__(
            cls,
            model: str,
            **kwargs
    ):
        if model not in cls.__AVAILABLE_MODELS:
            raise NameError(f'«{model}» model is not available')

        return object.__new__(cls)

    def __init__(
            self,
            model: str,
            **kwargs
    ):
        self.__model = self.__AVAILABLE_MODELS[model].__call__(**kwargs)

    @property
    def model(self):
        return self.__model
