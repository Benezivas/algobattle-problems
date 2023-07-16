"""Tests for the scheduling problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from algobattle_problems.scheduling.problem import Instance, Solution, ValidationError


class Tests(unittest.TestCase):
    """Tests for the scheduling problem."""

    @classmethod
    def setUpClass(cls):
        cls.instance = Instance(job_lengths=[30, 120, 24, 40, 60])

    def test_solution_wrong_length(self):
        with self.assertRaises(ValidationError):
            Solution(assignments=[]).validate_solution(self.instance)

    def test_solution_wrong_machine(self):
        with self.assertRaises(PydanticValidationError):
            Solution(assignments=[0, 0, 0, 0, 0])

    def test_solution_makespan(self):
        solution = Solution(assignments=[4, 1, 5, 3, 2])
        self.assertEqual(solution.score(self.instance), 120)


if __name__ == "__main__":
    unittest.main()
