# Documentation

### switch

**sweetcase.switch**(expression, cases)

The switch function evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

Parameters:
* expression - Expression for the switch evaluation.
* cases - List of objects of the type Case, which is returned from the case() function.

<br/><br/>

### case

**sweetcase.case**(value, statement)

The case functions returns a Case object, that can be used for the cases array received by the switch function.

Parameters:
* value -  Value to be compared to the switch's expression.
* statement - A function of a lambda to be operated if the value matches the switch's expression.
* arguments - (Optional, default = []) A list of arguments to send the statement function.
* to_break - (Optional, default = True) Boolean value which when true, breaks the switch after running the statement of a matching case.
* multi_case - (Optional, default = False) Boolean value which when true, sweetcase will expect a list for case value, and during evaluation each value in the list will be compared with the expression separately.  
