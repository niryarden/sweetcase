from .exceptions import EternalLoopError, ArgumentParameterError
from .utils import length


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
    elif type(arguments) != list:
        raise ArgumentParameterError("Arguments parameter must be type list")
    elif statement.__code__.co_argcount - length(statement.__defaults__) != length(arguments):
        raise ArgumentParameterError("Arguments amount does not fit statement function")

    if multi_case:
        if goto in value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")
    else:
        if goto == value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")

    return Case(value, statement, arguments, to_break, multi_case, goto)
