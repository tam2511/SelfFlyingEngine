from src.api import TelloAPI
from typing import Any


class Quadcopter(object):
    """
    Класс Quadcopter предназначен для создания экземпляров классов из пакета src/api.
    Созданные экземпляры представляют собой API соответствующих моделей квадрокоптеров.
    В данный момент доступы следующие модели: "Trello".
    Класс Quadcopter является классом-фабрикой и не может быть инстанцирован.
    """
    __AVAILABLE_MODELS = {
        'Tello': TelloAPI
    }

    def __new__(
            cls,
            model: str,
            ip: str
    ) -> Any:
        if model not in cls.__AVAILABLE_MODELS:
            raise NameError(f'«{model}» model is not available')

        return cls.__AVAILABLE_MODELS[model].__call__(ip)
