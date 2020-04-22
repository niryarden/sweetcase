from sweetcase import switch, case, default


def main():
    expression = 4
    switch(expression, [
        case(4, lambda: print('4'), to_break=False),
        case(3 + 1, lambda: print('3 + 1'), to_break=False),
        case(default, lambda: print('error'))
    ])


if __name__ == "__main__":
    main()
