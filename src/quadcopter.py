from api import TelloAPI


class Quadcopter(object):
    def __init__(
            self,
            model: str,
    ):
        match model:
            case 'Tello':
                self.__model = TelloAPI()
            case _:
                raise NameError(f'«{model}» model not available')
