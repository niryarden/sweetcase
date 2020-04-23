import unittest
from sweetcase import switch, case, default


class TestGoto(unittest.TestCase):
    def test_no_goto(self):
        result = []

        def human_options():
            result.append("man")
            result.append("woman")
            result.append("child")

        def mammal_options():
            result.append("lion")
            result.append("whale")
            result.append("giraffe")

        def animal_options():
            result.append("bird")
            result.append("fish")
            result.append("ant")

        me = "human"
        switch(me, [
            case("human",
                 human_options),
            case("mammal",
                 mammal_options,
                 goto="human"),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: print("unknown"))
        ])

        self.assertEqual(result, ["man", "woman", "child"])

    def test_one_goto(self):
        result = []

        def human_options():
            result.append("man")
            result.append("woman")
            result.append("child")

        def mammal_options():
            result.append("lion")
            result.append("whale")
            result.append("giraffe")

        def animal_options():
            result.append("bird")
            result.append("fish")
            result.append("ant")

        me = "mammal"
        switch(me, [
            case("human",
                 human_options),
            case("mammal",
                 mammal_options,
                 goto="human"),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: print("unknown"))
        ])

        self.assertEqual(result, ["lion", "whale", "giraffe", "man", "woman", "child"])

    def test_chain_goto(self):
        result = []

        def human_options():
            result.append("man")
            result.append("woman")
            result.append("child")

        def mammal_options():
            result.append("lion")
            result.append("whale")
            result.append("giraffe")

        def animal_options():
            result.append("bird")
            result.append("fish")
            result.append("ant")

        me = "animal"
        switch(me, [
            case("human",
                 human_options),
            case("mammal",
                 mammal_options,
                 goto="human"),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: print("unknown"))
        ])

        self.assertEqual(result, ["bird", "fish", "ant", "lion", "whale", "giraffe", "man", "woman", "child"])

    def test_goto_multiple_cases(self):
        counter = 0

        def add_to_counter():
            nonlocal counter
            counter += 1

        expression = 4
        switch(expression, [
            case(4,
                 add_to_counter, goto=3),
            case(3,
                 add_to_counter),
            case(2 + 1,
                 add_to_counter),
            case(default,
                 lambda: add_to_counter)
        ])

        self.assertEqual(counter, 3)


if __name__ == "__main__":
    unittest.main()
