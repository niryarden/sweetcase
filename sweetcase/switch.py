from .default import default


def switch(condition, cases):
    default_value = False
    for case in cases:
        if condition == case.value:
            return case.exec()
        if case.value == default:
            default_value = case.func
    return default_value()
