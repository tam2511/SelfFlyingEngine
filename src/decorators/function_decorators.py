from functools import wraps


def ignored_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if self.autopilot is True:
            print(f'{self} ignored «{fn.__name__}»')
        else:
            return fn(self, *args, **kwargs)

    return wrapper


def available_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if self.access is False:
            raise PermissionError(f'{self} locked')

        return fn(self, *args, **kwargs)

    return wrapper
