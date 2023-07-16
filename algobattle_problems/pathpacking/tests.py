"""Tests for the Pathpacking problem."""
import unittest

from algobattle_problems.pathpacking.problem import UndirectedGraph, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the Pathpacking problem."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = UndirectedGraph(
            num_vertices=6,
            edges=[
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
            ],
        )

    def test_solution_empty(self):
        Solution(paths=set()).validate_solution(self.instance, Role.generator)

    def test_solution_not_path(self):
        with self.assertRaises(ValidationError):
            Solution(paths={(0, 2, 3)}).validate_solution(self.instance, Role.generator)

    def test_solution_not_disjoint(self):
        with self.assertRaises(ValidationError):
            Solution(paths={(0, 1, 2), (2, 3, 4)}).validate_solution(self.instance, Role.generator)

    def test_score(self):
        self.assertEqual(Solution(paths={(0, 1, 2)}).score(self.instance), 1)
        self.assertEqual(Solution(paths={(0, 1, 2), (3, 4, 5)}).score(self.instance), 2)


if __name__ == "__main__":
    unittest.main()
