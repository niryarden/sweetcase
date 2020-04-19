# example use of the sweetcase module
# the following code is equivalent to:

# switch(argument) {
#     case 1:
#         return "one";
#     case 2:
#         return "two";
#     case 3:
#         return "three";
#     default:
#         return "zero";
# };

from sweetcase import switch, case, default


def main():
    num = int(input(">> "))

    res = switch(num, [
        case(1, lambda: 'one'),
        case(2, lambda: 'two'),
        case(3, lambda: 'three'),
        case(default, lambda: 'zero')
    ])

    print(res)


if __name__ == "__main__":
    main()
