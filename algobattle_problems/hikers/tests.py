"""Tests for the hikers problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from algobattle_problems.hikers.problem import HikersInstance, Solution, ValidationError, Role


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
        Solution.model_validate({"assignments": {}}, context={"instance": self.instance})

    def test_solution_correct(self):
        solution = Solution(
            assignments={
                2: 1,
                0: 2,
                3: 2,
                4: 2,
            }
        )
        solution.validate_solution(self.instance, Role.generator)

    def test_solution_wrong_hiker(self):
        with self.assertRaises(PydanticValidationError):
            Solution.model_validate({"assignments": {10: 1}}, context={"instance": self.instance})

    def test_solution_hiker_unhappy(self):
        with self.assertRaises(ValidationError):
            sol = Solution.model_validate({"assignments": {1: 1}}, context={"instance": self.instance})
            sol.validate_solution(self.instance, Role.generator)


if __name__ == "__main__":
    unittest.main()
