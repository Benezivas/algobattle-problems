"""Tests for the c4subgraphiso problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from ..problems.c4subgraphiso.problem import C4subgraphiso, ValidationError


class SolutionTests(unittest.TestCase):
    """Tests for the c4subgraphiso verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.instance = C4subgraphiso(num_vertices=10, edges=[
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
        ])

    def test_no_duplicate_squares(self):
        with self.assertRaises(PydanticValidationError):
            C4subgraphiso.parse_obj({
                "squares": {
                    (0, 1, 2, 3),
                    (0, 1, 2, 3),
                }
            })

    def test_vertex_too_big(self):
        solution = C4subgraphiso.Solution(squares={(0, 1, 2, 10)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

    def test_edge_missing(self):
        solution = C4subgraphiso.Solution(squares={(2, 3, 4, 5)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

    def test_additional_edge(self):
        solution = C4subgraphiso.Solution(squares={(1, 2, 4, 8)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

    def test_score(self):
        solution = C4subgraphiso.Solution(squares={(0, 1, 8, 9), (4, 5, 6, 7)})
        solution.validate_solution(self.instance, 10)
        self.assertEqual(solution.score(10, self.instance), 2)

    def test_squares_disjoin(self):
        solution = C4subgraphiso.Solution(squares={(0, 1, 2, 3), (0, 1, 8, 9)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

if __name__ == '__main__':
    unittest.main()
