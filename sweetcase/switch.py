from .default import default


def switch(expression, cases):
    default_value = False
    should_execute_default = True

    for case in cases:
        if expression == case.value:
            if case.to_break:
                return case.exec()
            else:
                case.exec()
                # if a case statement was already executed (without breaking the switch), don't run default in the end
                should_execute_default = False
        if case.value == default:
            default_value = case.statement

    if should_execute_default and default_value:
        return default_value()
    else:
        return None
