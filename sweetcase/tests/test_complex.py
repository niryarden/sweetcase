import unittest
from sweetcase import switch, case, default


class TestComplex(unittest.TestCase):
    def test_multicase_of_types_with_argument(self):
        result = None

        def update_result(new_result):
            nonlocal result
            result = new_result

        data = {"sweet": "case", "git": "hub"}
        switch(type(data), [
            case([str, list],
                 update_result, arguments=[len(data)], multi_case=True),
            case(dict,
                 update_result, arguments=[len(data.keys())]),
            case(type(None),
                 update_result, arguments=[None]),
            case([int, default],
                 update_result, arguments=[data], multi_case=True),
        ])

        self.assertEqual(result, 2)

    def test_bigger_than(self):
        result = None

        def update_result(new_result):
            nonlocal result
            result = new_result

        num = 105
        switch(True, [
            case(num < 10,
                 update_result, arguments=["one digit"]),
            case(9 < num < 100,
                 update_result, arguments=["two digits"]),
            case(num > 99,
                 update_result, arguments=["three digits"]),
            case(default,
                 update_result, arguments=["off-limit"]),
        ])

        self.assertEqual(result, "three digits")


if __name__ == "__main__":
    unittest.main()
