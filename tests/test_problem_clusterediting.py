"""Tests for the clusterediting problem."""
import unittest

from algobattle_problems.clusterediting.problem import Clusterediting, ValidationError


Solution = Clusterediting.Solution


class SolutionTests(unittest.TestCase):
    """Tests for the clusterediting solutions."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Clusterediting(num_vertices=10, edges=[
            (0, 2),
            (0, 5),
            (0, 8),
            (1, 5),
            (1, 7),
            (1, 8),
            (2, 3),
            (2, 5),
            (2, 6),
            (3, 6),
            (4, 8),
        ])

    def test_delete_nonexisting_edge(self):
        solution = Solution(add=set(), delete={(0, 1)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

    def test_delete_extra_edge(self):
        solution = Solution(add=set(), delete={(0, 2)})
        solution.validate_solution(self.instance, 10)

    def test_delete_and_add_edge(self):
        solution = Solution(add={(0, 3)}, delete={(0, 2)})
        solution.validate_solution(self.instance, 10)

    def test_add_edge_reverse(self):
        solution = Solution(add={(2, 0)}, delete=set())
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

    def test_delete_edge_reverse(self):
        solution = Solution(add=set(), delete={(2, 0)})
        solution.validate_solution(self.instance, 10)

    def test_score(self):
        solution = Solution(add={(0, 1), (5, 8)}, delete={(4, 8), (7, 1), (0, 2), (2, 5)})
        solution.validate_solution(self.instance, 10)
        self.assertEqual(solution.score(10, self.instance), 6)

    def test_solution_doesnt_triangulate(self):
        solution = Solution(add={(0, 1), (5, 8)}, delete={(7, 1), (0, 2), (2, 5)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, 10)

if __name__ == '__main__':
    unittest.main()
