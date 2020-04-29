# Documentation

## switch

**sweetcase.switch**(expression, cases)

The switch function evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

Parameters:
* expression - Expression for the switch evaluation.
* cases - List of objects of the type `Case`, which is returned from the `case()` function.

<br/><br/>

## case

**sweetcase.case**(value, statement, arguments=[], to_break=True, multi_case=False, goto=None, regex=False)

The case functions returns a Case object, that can be used in the cases array supplied to the switch function.

Parameters:
* **value** -  Value to be compared to the switch's expression.
* **statement** - A function or a lambda to be executed if the value matches the switch's expression.
* **arguments** - (Optional, default = []) A list of arguments to send the statement function, single argument should be supplied inside a list as well. Please notice that arguments whose default values defined in the function can't be passed to the case, and these arguments of the function are ignored by the switch. 
* **to_break** - (Optional, default = True) Boolean value which when true, breaks the switch after executing the statement of a matching case. please notice that this behavior is different from classic switch-case syntax, in which the lack of break in the end of a statement results the interpreter to run the next case's statement, regardless of its value. In sweetcase, to_break=False for a matching value means that the switch won't break and will keep looking for more matching cases.
* **multi_case** - (Optional, default = False) Boolean value which when true, sweetcase will expect a list for the case value, and during evaluation each value in the list will be compared with the expression separately. That allows setting the same statement for multiple values.
* **goto** - (Optional, default = None) An object that will be equal to the value of another case supplied to the switch. After the statement was executed, the switch will additionally execute every case whose value matches the original case's goto. Please notice that, naturally, adding a goto parameter to a case will automatically change its to_break parameter to false, in order to allow the switch to operate additional cases without breaking.
* **regex** - (Optional, default = False) Boolean value which when True, sweetcase will expect the case's value to be a string (or list of strings, if multi_case=True), and will compare it to the expression using [re.search](https://docs.python.org/3/library/re.html#re.search) instead of using basic 'equals' (==). 

<br/><br/><br/>

Please check out our [USAGE_EXAMPLES.md](https://github.com/niryarden/sweetcase/blob/master/USAGE_EXAMPLES.md) to explore the usages of all functions and parameters.
