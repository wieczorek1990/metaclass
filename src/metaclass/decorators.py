def metaclass(**kwargs):
    class Meta:  # pylint: disable=R0903
        pass

    for key, value in kwargs.items():
        setattr(Meta, key, value)

    def decorator(function):
        setattr(function, "Meta", Meta)
        return function

    return decorator
