"""Tests for the hikers problem."""
import unittest

from algobattle_problems.hikers.problem import HikersInstance, Solution, ValidationError


class Tests(unittest.TestCase):
    """Tests for the hikers problem."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = HikersInstance(
            hikers=[
                (1, 3),
                (10, 12),
                (1, 1),
                (2, 5),
                (3, 3),
            ]
        )

    def test_solution_empty(self):
        solution = Solution(assignments={})
        solution.validate_solution(self.instance)

    def test_solution_correct(self):
        solution = Solution(
            assignments={
                2: 1,
                0: 2,
                3: 2,
                4: 2,
            }
        )
        solution.validate_solution(self.instance)

    def test_solution_wrong_hiker(self):
        solution = Solution(assignments={10: 1})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance)

    def test_solution_hiker_unhappy(self):
        solution = Solution(assignments={1: 1})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance)


if __name__ == "__main__":
    unittest.main()
