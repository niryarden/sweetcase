import unittest
from sweetcase import switch, case, default


class TestBasic(unittest.TestCase):
    def test_basic_use(self):
        num = 2
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
        self.assertEqual(res, "two", "Should be two")

    def test_basic_use2(self):
        operator = "*"
        n1 = 8
        n2 = 2

        res = switch(operator, [
            case("+",
                 lambda: f"{n1} {operator} {n2} = {n1 + n2}"),
            case("-",
                 lambda: f"{n1} {operator} {n2} = {n1 - n2}"),
            case("*",
                 lambda: f"{n1} {operator} {n2} = {n1 * n2}"),
            case("/",
                 lambda: f"{n1} {operator} {n2} = {n1 / n2}"),
            case(default,
                 lambda: f"unsupported operator"),
        ])
        self.assertEqual(res, "8 * 2 = 16")

    def test_basic_default(self):
        num = "random"
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
        self.assertEqual(res, "zero", "Should be zero")

    def test_middle_default(self):
        num = "random"
        res = switch(num, [
            case(1,
                 lambda: "one"),
            case(default,
                 lambda: "zero"),
            case(2,
                 lambda: "two"),
            case(3,
                 lambda: "three")

        ])
        self.assertEqual(res, "zero", "Should be zero")

    def test_beginning_default(self):
        num = "random"
        res = switch(num, [
            case(default,
                 lambda: "zero"),
            case(1,
                 lambda: "one"),
            case(2,
                 lambda: "two"),
            case(3,
                 lambda: "three")

        ])
        self.assertEqual(res, "zero", "Should be zero")


if __name__ == "__main__":
    unittest.main()
