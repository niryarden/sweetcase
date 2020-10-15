import unittest
import operator
import io
import sys
from sweetcase import switch, case, default
from sweetcase.exceptions import ArgumentParameterError


class TestArguments(unittest.TestCase):
    def test_arguments_to_func(self):
        result = None

        def calc(num1, num2, math_operator):
            nonlocal result
            result = math_operator(num1, num2)

        num1 = 10
        num2 = 8
        math_operator = "-"
        switch(math_operator, [
            case("+",
                 calc, arguments=[num1, num2, operator.__add__]),
            case("-",
                 calc, arguments=[num1, num2, operator.__sub__]),
            case("*",
                 calc, arguments=[num1, num2, operator.__mul__])
        ])

        self.assertEqual(result, 2)

    def test_broken_arguments_to_func(self):
        result = None

        def calc(num1, num2, math_operator):
            nonlocal result
            result = math_operator(num1, num2)

        num1 = 10
        num2 = 8
        math_operator = "-"
        with self.assertRaises(ArgumentParameterError):
            switch(math_operator, [
                case("+",
                     calc, arguments=[num1, num2, operator.__add__]),
                case("+",
                     calc, arguments=[num1, num2]),
                case("+",
                     calc, arguments=[num1, num2, operator.__mul__])
            ])

        self.assertIsNone(result)

    def test_arguments_to_builtinFunc(self):
        saved_stdout = sys.stdout
        with io.StringIO() as capturedOutput:
            sys.stdout = capturedOutput
            num = 3
            switch(True, [
                case(num > 100,
                     print, arguments=["above 100"]),
                case(num > 50,
                     print, arguments=["above 50"]),
                case(num > 0,
                     print, arguments=["above 0"]),
                case(default,
                     print, arguments=["negative"])
            ])

            output = capturedOutput.getvalue().strip()
            sys.stdout = saved_stdout

        self.assertEqual(output, "above 0")


if __name__ == "__main__":
    unittest.main()
