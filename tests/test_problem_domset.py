"""Tests for the DomSet problem."""
import unittest
import logging

from algobattle_problems.domset.problem import Domset, ValidationError

logging.disable(logging.CRITICAL)


class Verifiertests(unittest.TestCase):
    """Tests for the DomSet problem."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Domset(
            num_vertices=5,
            edges=[
                (0, 1),
                (2, 1),
                (2, 3),
                (3, 0),
            ],
        )

    def test_basic_validate(self):
        solution = Domset.Solution(domset={1, 3, 4})
        solution.validate_solution(self.instance, 5)

    def test_validate_missing_vertex(self):
        solution = Domset.Solution(domset={1, 3})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 5)

    def test_score(self):
        bad_solution = Domset.Solution(domset={0, 1, 2, 3, 4})
        good_solution = Domset.Solution(domset={1, 3, 4})
        self.assertEqual(bad_solution.score(self.instance, 5), 5)
        self.assertEqual(good_solution.score(self.instance, 5), 3)
        self.assertEqual(
            self.instance.calculate_score(bad_solution, good_solution, 5), 0.6
        )


if __name__ == "__main__":
    unittest.main()
