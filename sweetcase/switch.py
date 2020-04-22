from .default import default


def switch(expression, cases):
    default_value = False
    should_execute_default = True

    for case in cases:
        if get_comparison_condition(expression, case):
            if case.to_break:
                return case.exec()
            else:
                case.exec()
                # if a case statement was already executed (without breaking the switch), don't run default in the end
                should_execute_default = False

        if get_default_check_condition(case):
            default_value = case.exec

    if should_execute_default and default_value:
        return default_value()
    else:
        return None


def get_comparison_condition(expression, case):
    if case.multi_case and type(case.value) == list:
        return expression in case.value
    if not case.multi_case:
        return expression == case.value
    return False


def get_default_check_condition(case):
    if case.multi_case and type(case.value) == list:
        return default in case.value
    if not case.multi_case:
        return default == case.value
    return False
