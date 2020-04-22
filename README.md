# sweetcase
Light-weight module allowing the use a [switch-case](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch) alike syntax for python.

<br/>

### Install and Import

```bash
pip install sweetcase
```

```python
from sweetcase import switch, case, default
```
<br/>

### Usage Examples
(1) use:
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

to achieve the equivalent behavior of:
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

(2) multiline function and arguments example:
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
    case("+", addition, arguments),
    case("-", subtraction, arguments),
    case(default, lambda: 'error', arguments)
])

print(f"{arguments[0]} + {arguments[1]} = {res}")
```
<br/>

### Documentation
**sweetcase.switch(expression, cases)**

The switch function evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

Parameters:
* expression - Expression for the switch evaluation.
* cases - List of objects of the type Case, which is returned from the case() function.

<br/><br/>

**sweetcase.case(value, statement)**

The case functions returns a Case object, that can be used for the cases array received by the switch function.

Parameters:
* value -  Value to be compared to the switch's expression.
* statement - A function of a lambda to be operated if the value matches the switch's expression.
* arguments - (Optional, default = []) A list of arguments to send the statement function.
