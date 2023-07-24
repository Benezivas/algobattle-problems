"""Tests for the Pairsum problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from algobattle_problems.pairsum.problem import Instance, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the Pairsum Verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Instance(numbers=[1, 2, 3, 4])

    def test_size(self):
        self.assertEqual(self.instance.size, 4)
        self.assertEqual(Instance(numbers=[1, 2, 3, 4, 5, 6]).size, 6)
        self.assertEqual(Instance(numbers=list(range(17))).size, 17)

    def test_solution_wrong_indices(self):
        with self.assertRaises(PydanticValidationError):
            Solution.create_and_validate({"indices": (100, 101, 102, 103)}, instance=self.instance)

    def test_solution_duplicate_index(self):
        with self.assertRaises(PydanticValidationError):
            Solution.create_and_validate({"indices": (0, 0, 1, 2)}, instance=self.instance)

    def test_solution_wrong_sum(self):
        with self.assertRaises(ValidationError):
            Solution(indices=(0, 1, 2, 3)).validate_solution(self.instance, Role.generator)


if __name__ == "__main__":
    unittest.main()
