from .exceptions import EternalLoopError


class Case:
    def __init__(self, value, statement, arguments, to_break, multi_case, goto):
        self.value = value
        self.statement = statement
        self.arguments = arguments
        self.to_break = to_break
        self.multi_case = multi_case
        self.goto = goto

    def exec(self):
        return self.statement(*self.arguments)


def case(value, statement, arguments=None, to_break=True, multi_case=False, goto=None):
    if arguments is None:
        arguments = []

    if multi_case:
        if goto in value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")
    else:
        if goto == value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")

    return Case(value, statement, arguments, to_break, multi_case, goto)
