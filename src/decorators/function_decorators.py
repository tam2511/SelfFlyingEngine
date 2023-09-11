from functools import wraps


def available_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if (
            self.access is False
            or self.autopilot is True
        ):
            raise PermissionError(f'{self} locked')

        return fn(self, *args, **kwargs)

    return wrapper
