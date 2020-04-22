from sweetcase import switch, case, default


def main():
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


if __name__ == "__main__":
    main()
