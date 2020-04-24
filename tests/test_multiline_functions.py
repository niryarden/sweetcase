import unittest
from sweetcase import switch, case


class TestMultilineFunctions(unittest.TestCase):
    def test_basic_multiline_functions(self):
        num1 = 7
        num2 = 5

        def addition():
            result = num1 + num2
            return result

        def subtraction():
            result = num1 - num2
            return result

        action = "+"
        res = switch(action, [
            case("+",
                 addition),
            case("-",
                 subtraction)
        ])

        self.assertEqual(res, 12, 'Should be 12')

    def test_multiline_with_arguments(self):
        def addition(num1, num2):
            result = num1 + num2
            return result

        def subtraction(num1, num2):
            result = num1 - num2
            return result

        numbers = [7, 5]
        action = "-"
        res = switch(action, [
            case("+",
                 addition, arguments=numbers),
            case("-",
                 subtraction, arguments=numbers)
        ])

        self.assertEqual(res, 2, 'Should be 2')


if __name__ == "__main__":
    unittest.main()
