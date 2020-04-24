# Usage Examples

## Basic use
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
c
```

Using this work-around, you can use more complex case values:
```python
num = 105
switch(True, [
    case(num < 10,
         lambda: print("one digit")),
    case(9 < num < 100,
         lambda: print("two digits")),
    case(num > 99,
         lambda: print("three digits")),
    case(default,
         lambda: print("off-limit")),
])
```

<br/><br/>

## Use of multiline function with arguments
```python
def addition(num1, num2):
    result = num1 + num2
    print("executing addition")
    return result

def subtraction(num1, num2):
    result = num1 - num2
    print("executing subtraction")
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

## Use of to_break=False
the output will be both '4', '3 + 1' and '2 + 2'
```python
expression = 4
switch(expression, [
    case(4,
         lambda: print("4"), to_break=False),
    case(3 + 1,
         lambda: print("3 + 1"), to_break=False),
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

_**The behavior of sweetcase's break is different from the classic switch-case behavior. Please see our [DOCS.md](https://github.com/niryarden/sweetcase/blob/master/DOCS.md) for further details.**_ 

Another example (output will be `['August', 'September', 'October', 'November', 'December']`):
```python
future_months = []
current_month = 8

switch(True, [
    case(current_month <= 1,
         lambda: future_months.append("January"), to_break=False),
    case(current_month <= 2,
         lambda: future_months.append("February"), to_break=False),
    case(current_month <= 3,
         lambda: future_months.append("March"), to_break=False),
    case(current_month <= 4,
         lambda: future_months.append("April"), to_break=False),
    case(current_month <= 5,
         lambda: future_months.append("May"), to_break=False),
    case(current_month <= 6,
         lambda: future_months.append("June"), to_break=False),
    case(current_month <= 7,
         lambda: future_months.append("July"), to_break=False),
    case(current_month <= 8,
         lambda: future_months.append("August"), to_break=False),
    case(current_month <= 9,
         lambda: future_months.append("September"), to_break=False),
    case(current_month <= 10,
         lambda: future_months.append("October"), to_break=False),
    case(current_month <= 11,
         lambda: future_months.append("November"), to_break=False),
    case(current_month <= 12,
         lambda: future_months.append("December")),
])
```

equivalent java code:
```java
java.util.ArrayList<String> futureMonths = new java.util.ArrayList<String>();
int month = 8;

switch (month) {
    case 1:  futureMonths.add("January");
    case 2:  futureMonths.add("February");
    case 3:  futureMonths.add("March");
    case 4:  futureMonths.add("April");
    case 5:  futureMonths.add("May");
    case 6:  futureMonths.add("June");
    case 7:  futureMonths.add("July");
    case 8:  futureMonths.add("August");
    case 9:  futureMonths.add("September");
    case 10: futureMonths.add("October");
    case 11: futureMonths.add("November");
    case 12: futureMonths.add("December");
             break;
```

<br/><br/>

## Use of multi-case

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
output will be all 9 animals printed:
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
The default case will be executed if no other case matched the switch expression. Default's location won't effect the output (in the following example - 0). To use default, import it from sweetcase.
```python
from sweetcase import switch, case, default

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
Another useful example is using the type of a variable as the expression of the switch:
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

<br /><br />

## Local Variable as Output 
```python
result = None

def update_result(new_result):
    nonlocal result
    result = new_result

name = "george"
switch(name, [
    case("paul",
         update_result, arguments=["yesterday"]),
    case("john",
         update_result, arguments=["strawberry fields forever"]),
    case("george",
         update_result, arguments=["while my guitar gently weeps"]),
    case("ringo",
         update_result, arguments=["with a little help from my friend"]),
    case(default,
         update_result, arguments=["unknown"])
])
```
