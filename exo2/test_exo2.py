import unittest
from exo2 import Solution

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs")
)


class TestSolution(unittest.TestCase):
    def test_fixed_cases_true(self):
        for test in fixed_tests_True:
            with self.subTest(string=test[0], ending=test[1]):
                self.assertTrue(Solution.solution(test[0], test[1]))

    def test_fixed_cases_false(self):
        for test in fixed_tests_False:
            with self.subTest(string=test[0], ending=test[1]):
                self.assertFalse(Solution.solution(test[0], test[1]))


if __name__ == '__main__':
    unittest.main()
