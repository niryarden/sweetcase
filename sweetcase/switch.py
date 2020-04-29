import inspect
import re
from sweetcase.default import default


def switch(expression, cases):
    check_supplied_parameters_to_switch(expression, cases)
    return run_switch(expression, cases)


def check_supplied_parameters_to_switch(expression, cases):
    if type(cases) != list:
        raise TypeError("cases parameter must be type list")

    if callable(expression) and not inspect.isclass(expression):
        raise TypeError("expression must not be function or lambda, as they are not comparable")


def run_switch(expression, cases):
    default_value = False
    should_execute_default = True

    for case in cases:
        if get_comparison_condition(expression, case):
            if case.goto:
                return handle_goto(case, cases)
            elif case.to_break:
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
        if case.regex:
            # create a regex which is a combination of all regex cases
            combined_regex = "(" + ")|(".join(case.value) + ")"
            return bool(re.search(combined_regex, expression))
        else:
            return expression in case.value
    if not case.multi_case:
        if case.regex:
            return bool(re.search(case.value, expression))
        else:
            return expression == case.value
    return False


def get_default_check_condition(case):
    if case.multi_case and type(case.value) == list:
        return default in case.value
    if not case.multi_case:
        return default == case.value
    return False


def handle_goto(current_case, cases):
    current_case.exec()
    if current_case.goto:
        goto_matches = [
            potential_case for potential_case in cases if get_comparison_condition(current_case.goto, potential_case)]
        for goto in goto_matches:
            handle_goto(goto, cases)
