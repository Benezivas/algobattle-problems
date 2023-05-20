"""Tests for the Pairsum problem."""
import unittest

from algobattle_problems.pairsum.problem import Pairsum, ValidationError


class Tests(unittest.TestCase):
    """Tests for the Pairsum Verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Pairsum(numbers=[1, 2, 3, 4])

    def test_size(self):
        self.assertEqual(self.instance, 4)
        self.assertEqual(Pairsum(numbers=[]), 0)
        self.assertEqual(Pairsum(numbers=[1]), 0)

    def test_solution_wrong_indices(self):
        with self.assertRaises(ValidationError):
            Pairsum.Solution(indices=(100, 101, 102, 103)).validate_solution(self.instance)

    def test_solution_duplicate_index(self):
        with self.assertRaises(ValidationError):
            Pairsum.Solution(indices=(0, 0, 1, 2)).validate_solution(self.instance)

    def test_solution_wrong_sum(self):
        with self.assertRaises(ValidationError):
            Pairsum.Solution(indices=(0, 1, 2, 3)).validate_solution(self.instance)


if __name__ == '__main__':
    unittest.main()
