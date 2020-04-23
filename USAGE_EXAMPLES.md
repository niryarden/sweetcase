# Usage Examples

## Basic use:
```python
from sweetcase import switch, case, default

num = 1
res = switch(num, [
    case(1,
         lambda: "one"),
    case(2,
         lambda: "two"),
    case(3,
         lambda: "three"),
    case(default,
         lambda: "zero")
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

## Use of to_break=False:
the output will be both '4', '3 + 1' and '2 + 2'
```python
expression = 4
switch(expression, [
    case(4,
         lambda: print("4"),
         to_break=False),
    case(3 + 1,
         lambda: print("3 + 1"),
         to_break=False),
    case(2 + 2,
         lambda: print("2 + 2"))
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
    case 2 + 2:
        console.log('2 + 2');
}
```

The behavior of sweetcase's break is different from the classic switch-case behavior. Please see our [DOCS.md](https://github.com/niryarden/sweetcase/blob/master/DOCS.md) for further details. 

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

<br/><br/>

## goto
output will be all 9 animals printed
```python
def human_options():
    print("man")
    print("woman")
    print("child")

def mammal_options():
    print("lion")
    print("whale")
    print("giraffe")

def animal_options():
    print("bird")
    print("fish")
    print("ant")

me = "animal"
switch(me, [
    case("human",
         human_options),
    case("mammal",
         mammal_options,
         goto="human"),
    case("animal",
         animal_options,
         goto="mammal"),
    case(default,
         lambda: print("unknown"))
])
```

equivalent c# code:
```c#
string me = "animal";
switch (me)
{
    case "human":
        Console.WriteLine("man");
        Console.WriteLine("woman");
        Console.WriteLine("child");
        break;
    case "mammal":
        Console.WriteLine("lion");
        Console.WriteLine("whale");
        Console.WriteLine("giraffe");
        goto "human";
    case "animal":
        Console.WriteLine("bird");
        Console.WriteLine("fish");
        Console.WriteLine("ant");
        goto "mammal";
}
```


<br/><br/>

## Default
Default's location won't effect the output (in that case - 0)
```python
foo = 4
switch(foo, [
    case(2,
         lambda: print(2)),
    case(3,
         lambda: print(3)),
    case(default,
         lambda: print(0)),
    case(4,
         lambda: print(4)),
    case(5,
         lambda: print(5))
])
```

equivalent JavaScript code:
```js
const foo = 6;
switch (foo) {
  case 2:
    console.log(2);
    break;
  case 3:
    console.log(3);
    break;
  default:
    console.log(0)
    break;
  case 4:
    console.log(4);
    break;
  case 5:
    console.log(5);
}
```

<br /><br />

## Type as Expression
Another useful example is using the type of a variable as the expression
```python
data = ["sweet", "case"]
switch(type(data), [
    case(int,
         lambda: print(data)),
    case([str, list],
         lambda: print(len(data)), multi_case=True),
    case(dict,
         lambda: print(len(data.keys()))),
    case(type(None),
         lambda: print(None)),
    case(default,
         lambda: print(data))
])
```

equivalent JavaScript code:
```js
const data = ['sweet', 'case'];
switch (data.type) {
  case 'int':
    console.log(data);
    break;
  case 'string':
  case 'array':
    console.log(data.length);
    break;
  case 'object':
    console.log(Object.keys(data).length);
    break;
  case 'null':
    console.log(null);
    break;
  default:
    console.log(data)
}
```
