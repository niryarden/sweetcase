class Case:
    def __init__(self, value, func):
        self.value = value
        self.func = func

    def exec(self):
        return self.func()


def case(value, func):
    return Case(value, func)
