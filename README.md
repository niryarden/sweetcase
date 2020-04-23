# sweetcase
Simple and light-weight module allowing the use of a **switch-case** alike syntax in python.

switch-case is a very common and useful syntax in many programming languages such as [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch), [C#](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/switch), [Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html), [C++](https://en.cppreference.com/w/cpp/language/switch), [Go](https://tour.golang.org/flowcontrol/9) and [C](https://www.programiz.com/c-programming/c-switch-case-statement), however, it's missing in Python.
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

num = 1
res = switch(num, [
    case(1,
         lambda: 'one'),
    case(2,
         lambda: 'two'),
    case(3,
         lambda: 'three'),
    case(default,
         lambda: 'zero')
])
```

equivalent JavaScript code:
```js
const myFunc = num => {
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
}
res = myFunc(1)
```
<br/>

sweetcase supports many more common uses of switch-case like **_break_**, **_arguments_** and **_multi-case_**. Please check out our [USAGE_EXAMPLES.md](https://github.com/niryarden/sweetcase/blob/master/USAGE_EXAMPLES.md) to explore these usages.

<br/>

## Documentation

Full documentation of the functions can be found in [DOCS.md](https://github.com/niryarden/sweetcase/blob/master/DOCS.md).
