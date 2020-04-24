import unittest
from sweetcase import switch, case, default


class TestMulticase(unittest.TestCase):
    def test_basic_multicase(self):
        animal = 'Dog'
        res = switch(animal, [
            case([
                "Cow",
                "Dog",
                "Pig"
            ], lambda: "This animal will go on Noah\'s Ark.", multi_case=True),
            case('Dove',
                 lambda: "This animal will come in the end."),
            case([
                "Dinosaur",
                default
            ], lambda: "This animal will not.", multi_case=True)
        ])

        self.assertEqual(res, "This animal will go on Noah\'s Ark.")

    def test_singlecase_next_to_multicase(self):
        animal = "Dove"
        res = switch(animal, [
            case([
                "Cow",
                "Dog",
                "Pig"
            ], lambda: "This animal will go on Noah\'s Ark.", multi_case=True),
            case('Dove',
                 lambda: "This animal will come in the end."),
            case([
                "Dinosaur",
                default
            ], lambda: "This animal will not.", multi_case=True)
        ])

        self.assertEqual(res, "This animal will come in the end.")

    def test_default_as_multicase(self):
        animal = default
        res = switch(animal, [
            case([
                "Cow",
                "Dog",
                "Pig"
            ], lambda: "This animal will go on Noah\'s Ark.", multi_case=True),
            case('Dove',
                 lambda: "This animal will come in the end."),
            case([
                "Dinosaur",
                default
            ], lambda: "This animal will not.", multi_case=True)
        ])

        self.assertEqual(res, "This animal will not.")

    def test_multicase_with_default(self):
        animal = "Dinosaur"
        res = switch(animal, [
            case([
                "Cow",
                "Dog",
                "Pig"
            ], lambda: "This animal will go on Noah\'s Ark.", multi_case=True),
            case('Dove',
                 lambda: "This animal will come in the end."),
            case([
                "Dinosaur",
                default
            ], lambda: "This animal will not.", multi_case=True)
        ])

        self.assertEqual(res, "This animal will not.")

    def test_array_value_not_multicase(self):
        names = ["john", "george", "ringo", "paul"]
        res = switch(names, [
            case(["john"],
                 lambda: "one beatle"),
            case(["john", "george"],
                 lambda: "two beatles"),
            case(["john", "george", "ringo"],
                 lambda: "three beatles"),
            case(["john", "george", "ringo", "paul"],
                 lambda: "all beatles"),
        ])

        self.assertEqual(res, "all beatles")


if __name__ == "__main__":
    unittest.main()
