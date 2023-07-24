"""Tests for the c4subgraphiso problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from algobattle_problems.c4subgraphiso.problem import UndirectedGraph, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the c4subgraphiso verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.instance = UndirectedGraph(
            num_vertices=10,
            edges=[
                (0, 1),
                (1, 2),
                (2, 3),
                (2, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 0),
                (1, 8),
                (4, 8),
                (4, 7),
                (2, 8),
                (0, 3),
            ],
        )

    def test_no_duplicate_squares(self):
        with self.assertRaises(PydanticValidationError):
            UndirectedGraph.parse_obj(
                {
                    "squares": {
                        (0, 1, 2, 3),
                        (0, 1, 2, 3),
                    }
                }
            )

    def test_vertex_too_big(self):
        solution = Solution(squares={(0, 1, 2, 10)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_edge_missing(self):
        solution = Solution(squares={(2, 3, 4, 5)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_additional_edge(self):
        solution = Solution(squares={(1, 2, 4, 8)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_score(self):
        solution = Solution(squares={(0, 1, 8, 9), (4, 5, 6, 7)})
        solution.validate_solution(self.instance, Role.generator)
        self.assertEqual(solution.score(self.instance, Role.solver), 2)

    def test_squares_disjoin(self):
        solution = Solution(squares={(0, 1, 2, 3), (0, 1, 8, 9)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)


if __name__ == "__main__":
    unittest.main()
