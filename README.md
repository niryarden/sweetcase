# sweetcase
Simple and light-weight module allowing the use a **[switch-case](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)** alike syntax in python.
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
Basic Use:
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
