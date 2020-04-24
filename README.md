# sweetcase
Simple and light-weight module allowing the use of a **switch-case** alike syntax in python.

switch-case is a very common and useful syntax in many programming languages such as [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch), [C#](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/switch), [Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html), [C++](https://en.cppreference.com/w/cpp/language/switch), [Go](https://tour.golang.org/flowcontrol/9), [php](https://www.php.net/manual/en/control-structures.switch.php) and [C](https://www.programiz.com/c-programming/c-switch-case-statement), however, it's missing in Python.
sweetcase allows Python programmers using a very similar syntax and get the same result. 
<br/><br/><br/>

## Install and Import
(currently unavailable)
```bash
pip install sweetcase
```

```python
from sweetcase import switch, case, default
```

#### prerequisites
Just any version of python 3 - No need of any additional modules. 

<br/>

## Usage Examples
Basic Use:
```python
from sweetcase import switch, case, default

operator = "*"
n1 = 8
n2 = 2

res = switch(operator, [
    case("+",
         lambda: n1 + n2),
    case("-",
         lambda: n1 - n2),
    case("*",
         lambda: n1 * n2),
    case("/",
         lambda: n1 / n2),
    case(default,
         lambda: "unsupported operator"),
])
```

equivalent JavaScript code:
```js
const operator = "*"
const n1 = 8
const n2 = 2

const myFunc = () => {
    switch (operator) {
      case '+':
        return n1 + n2;
      case '-':
        return n1 + n2;
      case '*':
        return n1 + n2;
      case '/':
        return n1 + n2;
      default:
        return 'unsupported operator';   
    }
}
const res = myFunc()
```
<br/>

sweetcase supports many more common uses of switch-case like **_break_**, **_multi-case_** and **_goto_**. Please check out our [USAGE_EXAMPLES.md](https://github.com/niryarden/sweetcase/blob/master/USAGE_EXAMPLES.md) to explore the different usages.

<br/>

## Documentation

Full documentation of the functions can be found in [DOCS.md](https://github.com/niryarden/sweetcase/blob/master/DOCS.md).
