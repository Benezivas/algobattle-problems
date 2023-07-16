"""Tests for the clusterediting problem."""
import unittest

from algobattle_problems.clusterediting.problem import UndirectedGraph, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the clusterediting solutions."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = UndirectedGraph(
            num_vertices=10,
            edges=[
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
            ],
        )

    def test_delete_nonexisting_edge(self):
        solution = Solution(add=set(), delete={(0, 1)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_delete_extra_edge(self):
        instance = UndirectedGraph(num_vertices=4, edges=[(0, 1), (1, 2), (2, 0), (0, 3)])
        solution = Solution(add=set(), delete={(0, 3)})
        solution.validate_solution(instance, Role.generator)

    def test_delete_and_add_edge(self):
        instance = UndirectedGraph(num_vertices=4, edges=[(1, 2), (2, 0), (0, 3)])
        solution = Solution(add={(0, 1)}, delete={(0, 3)})
        solution.validate_solution(instance, Role.generator)

    def test_add_edge_reverse(self):
        solution = Solution(add={(2, 0)}, delete=set())
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)

    def test_delete_edge_reverse(self):
        instance = UndirectedGraph(num_vertices=3, edges=[(0, 1), (1, 2)])
        solution = Solution(add=set(), delete={(1, 0)})
        solution.validate_solution(instance, Role.generator)

    def test_score(self):
        solution = Solution(add={(0, 1), (5, 8)}, delete={(4, 8), (7, 1), (0, 2), (2, 5)})
        solution.validate_solution(self.instance, Role.generator)
        self.assertEqual(solution.score(self.instance), 1/6)

    def test_solution_doesnt_triangulate(self):
        solution = Solution(add={(0, 1), (5, 8)}, delete={(7, 1), (0, 2), (2, 5)})
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance, Role.generator)


if __name__ == "__main__":
    unittest.main()
