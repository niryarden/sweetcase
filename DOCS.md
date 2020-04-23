# Documentation

## switch

**sweetcase.switch**(expression, cases)

The switch function evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

Parameters:
* expression - Expression for the switch evaluation.
* cases - List of objects of the type `Case`, which is returned from the `case()` function.

<br/><br/>

## case

**sweetcase.case**(value, statement, arguments=[], to_break=True, multi_case=False)

The case functions returns a Case object, that can be used in the cases array supplied to the switch function.

Parameters:
* value -  Value to be compared to the switch's expression.
* statement - A function or a lambda to be operated if the value matches the switch's expression.
* arguments - (Optional, default = []) A list of arguments to send the statement function. (single argument should be supplied inside a list as well)
* to_break - (Optional, default = True) Boolean value which when true, breaks the switch after running the statement of a matching case. please notice that this behavior is a different from classic switch-case syntax, in which the lack of break in the end of a statement results the interpreter to run the next case's statement, regardless of its value, while in sweetcase, to_break=False for a matching value means that the switch will keep looking for more matching cases.
* multi_case - (Optional, default = False) Boolean value which when true, sweetcase will expect a list for the case value, and during evaluation each value in the list will be compared with the expression separately.  

<br/><br/><br/>

Please check out our [USAGE_EXAMPLES.md](https://github.com/niryarden/sweetcase/blob/master/USAGE_EXAMPLES.md) to explore the usages of all functions and parameters.
