from ..api import TelloAPI


class Quadcopter(object):
    AVAILABLE_MODELS = {
        'Tello': TelloAPI
    }

    def __new__(cls, model, **kwargs):
        try:
            quadcopter = cls.AVAILABLE_MODELS[model].__call__(**kwargs)
            quadcopter.connect()
        except Exception:
            raise ConnectionError
        else:
            self = object.__new__(cls)
            self.api = quadcopter

        return self
