from .default import default


def switch(expression, cases):
    default_value = False
    for case in cases:
        if expression == case.value:
            return case.exec()
        if case.value == default:
            default_value = case.statement
    return default_value()
