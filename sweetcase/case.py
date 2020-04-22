class Case:
    def __init__(self, value, statement, arguments):
        self.value = value
        self.statement = statement
        self.arguments = arguments

    def exec(self):
        return self.statement(*self.arguments)


def case(value, statement, arguments=[]):
    return Case(value, statement, arguments)
