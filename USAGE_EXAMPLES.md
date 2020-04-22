# Usage Examples

## Basic use:
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
        return 'one';
        break;
    case 2:
        return 'two';
        break;
    case 3:
        return 'three';
        break;
    default:
        return 'zero';
    };
}
res = myFunc(1)
```

<br/><br/>

## Use of multiline function with arguments:
```python
def addition(num1, num2):
    result = num1 + num2
    print(result)
    return result

def subtraction(num1, num2):
    result = num1 - num2
    print(result)
    return result

numbers = [5, 3]
action = "+"

res = switch(action, [
    case("+",
         addition, arguments=numbers),
    case("-",
         subtraction, arguments=numbers),
    case(default,
         lambda: 'error')
])
```

equivalent JavaScript code:
```js
const myFunc = (action, num1, num2) => {
    switch(action) {
        case '+':
            var result = num1 + num2;
            console.log(result);
            return result;
            break;
        case '-':
            var result = num1 - num2;
            console.log(result);
            return result;
            break;
        default:
            return 'error';
    };
}
res = myFunc(5, 3, '+')
```

<br/><br/>

## Use of break:
the output will be both '4' and '3 + 1'
```python
expression = 4
switch(expression, [
    case(4,
         lambda: print("4"),
         to_break=False),
    case(3 + 1,
         lambda: print("3 + 1"),
         to_break=False),
    case(default,
         lambda: print("no match"))
])
```

equivalent JavaScript code:
```js
const expression = 4;
switch(expression) {
    case 4:
        console.log('4');
    case 3 + 1:
        console.log('3 + 1');
    default:
        console.log('no match');
}
```

<br/><br/>

## Use of multi-case:

```python
animal = 'Dog'
switch(animal, [
    case([
        "Cow",
        "Dog",
        "Pig"
    ], lambda: print("This animal will go on Noah\'s Ark."), multi_case=True),
    case('Dove',
         lambda: print("This animal will come in the end.")),
    case([
        "Dinosaur",
        default
    ], lambda: print("This animal will not."), multi_case=True)
])
```

equivalent JavaScript code:
```js
var Animal = 'Dog';
switch (Animal) {
  case 'Cow':
  case 'Dog':
  case 'Pig':
    console.log('This animal will go on Noah\'s Ark.');
    break;
  case 'Dove':
    console.log('This animal will come in the end.');
    break;
  case 'Dinosaur':
  default:
    console.log('This animal will not.');
}
```