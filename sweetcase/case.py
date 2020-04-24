import inspect
from sweetcase.exceptions import EternalLoopError, ArgumentParameterError
from sweetcase.utils import length


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
    check_supplied_parameters_to_case(value, statement, arguments, to_break, multi_case, goto)
    return Case(value, statement, arguments, to_break, multi_case, goto)


def check_supplied_parameters_to_case(value, statement, arguments, to_break, multi_case, goto):
    # check supplied value
    if callable(value) and not inspect.isclass(value):
        raise TypeError("value must not be function or lambda, as they are not comparable")

    # check supplied statement
    if not callable(statement):
        raise TypeError("statement parameter must be callable (function / lambda)")

    # check supplied arguments
    if type(arguments) != list:
        raise ArgumentParameterError("Arguments parameter must be type list")
    elif statement.__code__.co_argcount - length(statement.__defaults__) != length(arguments):
        raise ArgumentParameterError("Arguments amount does not fit statement function")

    # check supplied to_break and multi-case
    if type(to_break) != bool:
        raise TypeError("to_break parameter must be boolean")

    if type(multi_case) != bool:
        raise TypeError("multi_case parameter must be boolean")

    # check supplied goto
    if multi_case:
        if type(value) != list:
            raise TypeError("when multi-case is true, value parameter must be a list")
        if goto in value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")
    else:
        if goto == value:
            raise EternalLoopError("Case goto parameter leads to its own value, causing eternal loop.")
