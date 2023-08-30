from functools import wraps
# from src.session import Session


def access_session(fn):
    """
    Данный декоратор применяется к методам в классах,
    давая к ним доступ только при наличии атрибута session = True у экземпляра.
    Предназначен для классов, использование объектов которых возможно только при активной сессии [класс Session].
    """
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if self.session is not True:
            raise PermissionError(f'{self} cannot be used outside of session')

        return fn(self, *args, **kwargs)

    return wrapper
