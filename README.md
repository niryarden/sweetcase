# sweetcase
Simple and light-weight module allowing the use a **[switch-case](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)** alike syntax in python.
<br/>

## Table of Contents 
- [sweetcase](#sweetcase)
    + [Install and Import](#install-and-import)
    + [Usage Examples](#usage-examples)
    + [Documentation](#documentation)

<br/>

## Install and Import

```bash
pip install sweetcase
```

```python
from sweetcase import switch, case, default
```

<br/>

## Usage Examples
(1) basic use:
```python
from sweetcase import switch, case, default

num = 1
res = switch(num, [
    case(1, lambda: 'one'),
    case(2, lambda: 'two'),
    case(3, lambda: 'three'),
    case(default, lambda: 'zero')
])
```

is equivalent to the behavior of:
```js
const num = 1;
switch(num) {
    case 1:
        return "one";
        break;
    case 2:
        return "two";
        break;
    case 3:
        return "three";
        break;
    default:
        return "zero";
};
```
<br/>

(2) multiline function with arguments:
```python
def addition(num1, num2):
    result = num1 + num2
    print(result)
    return result

def subtraction(num1, num2):
    result = num1 - num2
    print(result)
    return result

arguments = [5, 3]
action = input(">> ")

res = switch(action, [
    case("+", addition, arguments=arguments),
    case("-", subtraction, arguments=arguments),
    case(default, lambda: 'error')
])

print(f"{arguments[0]} + {arguments[1]} = {res}")
```
<br/>

(3) use of `to_break=False` (will print both '4' and '3 + 1'):
```python
expression = 4
switch(expression, [
    case(4, lambda: print('4'), to_break=False),
    case(3 + 1, lambda: print('3 + 1'), to_break=False),
    case(default, lambda: print('error'))
])
```
<br/>

## Documentation
**sweetcase.switch**(expression, cases)

The switch function evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

Parameters:
* expression - Expression for the switch evaluation.
* cases - List of objects of the type Case, which is returned from the case() function.

<br/><br/>

**sweetcase.case**(value, statement)

The case functions returns a Case object, that can be used for the cases array received by the switch function.

Parameters:
* value -  Value to be compared to the switch's expression.
* statement - A function of a lambda to be operated if the value matches the switch's expression.
* arguments - (Optional, default = []) A list of arguments to send the statement function.
* to_break - (Optional, default = True) Boolean value which when true, breaks the switch after running the statement of a matching case. 
