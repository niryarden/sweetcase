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

    def test_to_break_is_false2(self):
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

        self.assertEqual(future_months, ['August', 'September', 'October', 'November', 'December'])


if __name__ == "__main__":
    unittest.main()
