class Case:
    def __init__(self, value, statement, arguments, to_break, multi_case):
        self.value = value
        self.statement = statement
        self.arguments = arguments
        self.to_break = to_break
        self.multi_case = multi_case

    def exec(self):
        return self.statement(*self.arguments)


def case(value, statement, arguments=None, to_break=True, multi_case=False):
    if arguments is None:
        arguments = []
    return Case(value, statement, arguments, to_break, multi_case)
