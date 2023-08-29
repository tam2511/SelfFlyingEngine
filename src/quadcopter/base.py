from api import TelloAPI


class Quadcopter(object):
    """
    Класс Quadcopter предназначен для создания экземпляров классов из пакета api.
    Созданные экземпляры представляют собой API соответствующих моделей квадрокоптеров.
    В данный момент доступы следующие модели: "Trello".
    Класс Quadcopter является классом-фабрикой и не может быть инстанцирован.
    """
    def __new__(
            cls,
            model: str,
            ip: str
    ):
        match model:
            case 'Tello':
                return TelloAPI(ip)
            case _:
                raise NameError(f'«{model}» model not available')
