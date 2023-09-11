from src.api import TelloAPI
from inspect import currentframe


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
        frame = currentframe().f_back.f_code.co_qualname.split('.')[0]
        if frame not in ('Session', 'Control'):
            raise PermissionError('Unable to access model')

        return self.__model
