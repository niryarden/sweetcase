import unittest
from sweetcase import switch, case


class TestBreak(unittest.TestCase):
    def test_break_is_true(self):
        counter = 0

        def add_to_counter():
            nonlocal counter
            counter += 1

        expression = 4
        switch(expression, [
            case(4,
                 add_to_counter),
            case(3 + 1,
                 add_to_counter),
            case(3,
                 add_to_counter)
        ])

        self.assertEqual(counter, 1, 'Should be 1')

    def test_break_is_false(self):
        counter = 0

        def add_to_counter():
            nonlocal counter
            counter += 1

        expression = 4
        switch(expression, [
            case(4,
                 add_to_counter,
                 to_break=False),
            case(3 + 1,
                 add_to_counter,
                 to_break=False),
            case(3,
                 add_to_counter)
        ])

        self.assertEqual(counter, 2, 'Should be 2')


if __name__ == "__main__":
    unittest.main()
