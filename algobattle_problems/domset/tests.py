"""Tests for the DomSet problem."""
import unittest

from algobattle_problems.domset.problem import Domset, UndirectedGraph, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the DomSet problem."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = UndirectedGraph(
            num_vertices=5,
            edges=[
                (0, 1),
                (2, 1),
                (2, 3),
                (3, 0),
            ],
        )

    def test_basic_validate(self):
        solution = Solution(domset={1, 3, 4})
        solution.validate_solution(self.instance, Role.generator)

    def test_validate_missing_vertex(self):
        solution = Solution(domset={1, 3})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_score(self):
        bad_solution = Solution(domset={0, 1, 2, 3, 4})
        good_solution = Solution(domset={1, 3, 4})
        self.assertAlmostEqual(bad_solution.score(self.instance, Role.solver), 1 / 5)
        self.assertAlmostEqual(good_solution.score(self.instance, Role.generator), 1 / 3)
        self.assertAlmostEqual(
            Domset.score(self.instance, generator_solution=good_solution, solver_solution=bad_solution), 0.6
        )


if __name__ == "__main__":
    unittest.main()
