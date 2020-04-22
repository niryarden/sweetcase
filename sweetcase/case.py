class Case:
    def __init__(self, value, statement, arguments, to_break):
        self.value = value
        self.statement = statement
        self.arguments = arguments
        self.to_break = to_break

    def exec(self):
        return self.statement(*self.arguments)


def case(value, statement, arguments=None, to_break=True):
    if arguments is None:
        arguments = []
    return Case(value, statement, arguments, to_break)
