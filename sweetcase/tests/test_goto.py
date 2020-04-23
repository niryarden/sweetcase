import unittest
from sweetcase import switch, case, default
from ..exceptions import EternalLoopError


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
                 lambda: result.append("unknown"))
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
                 lambda: result.append("unknown"))
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
                 lambda: result.append("unknown"))
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

    def test_goto_to_nowhere(self):
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
                 goto="bird"),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: result.append("unknown"))
        ])

        self.assertEqual(result, ["lion", "whale", "giraffe"])

    def test_goto_multiecase(self):
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
            case(["mammal", "bird"],
                 mammal_options,
                 goto="human",
                 multi_case=True),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: result.append("unknown"))
        ])

        self.assertEqual(result, ["bird", "fish", "ant", "lion", "whale", "giraffe", "man", "woman", "child"])

    def test_goto_self_eternal_loop(self):
        result = []

        def mammal_options():
            result.append("lion")
            result.append("whale")
            result.append("giraffe")

        with self.assertRaises(EternalLoopError):
            case("mammal", mammal_options, goto="mammal")

    def test_goto_to_with_redundant_break_parameter(self):
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
                 goto="human",
                 to_break=False),
            case("animal",
                 animal_options,
                 goto="mammal"),
            case(default,
                 lambda: result.append("unknown"))
        ])

        self.assertEqual(result, ["lion", "whale", "giraffe", "man", "woman", "child"])



if __name__ == "__main__":
    unittest.main()
