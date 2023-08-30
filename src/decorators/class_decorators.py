from re import fullmatch


def decorating_all_public_methods(*decorators):
    """
    Данный декоратор классов принимает на вход любое количество декораторов,
    и декорирует ими все публичные методы класса.
    """
    def decorate(cls):
        for attr, anything in cls.__dict__.items():
            if fullmatch(r'[a-zA-Z].*', attr) and callable(anything):
                for decorator in decorators:
                    setattr(cls, attr, decorator(getattr(cls, attr)))

        return cls

    return decorate
