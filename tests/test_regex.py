import unittest
from sweetcase import switch, case, default


class TestRegex(unittest.TestCase):
    def test_regex(self):
        res = None

        def update_result(new_result):
            nonlocal res
            res = new_result

        last_name = "Hernandez"
        switch(last_name, [
            case("(?i)sson",
                 update_result, arguments=["Swedish"], regex=True),
            case("(?i)ez",
                 update_result, arguments=["Spanish"], regex=True),
            case("(?i)ang",
                 update_result, arguments=["Chinese"], regex=True),
            case(["nev", "nov"],
                 update_result, arguments=["Russian"], regex=True, multi_case=True),
            case(default,
                 update_result, arguments=["no match"])
        ])

        self.assertEqual(res, "Spanish")


if __name__ == "__main__":
    unittest.main()
