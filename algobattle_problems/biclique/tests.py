"""Tests for the biclique problem."""
import unittest

from algobattle_problems.biclique.problem import UndirectedGraph, Solution, ValidationError, Role


class Tests(unittest.TestCase):
    """Tests for the Biclique problem solution class."""

    def test_vertices_exist(self):
        """Tests that only valid vertex indices are allowed."""
        graph = UndirectedGraph(num_vertices=10, edges=[(i, j) for i in range(10) for j in range(i)])
        sol = Solution(s_1=set(), s_2={20})
        with self.assertRaises(ValidationError):
            sol.validate_solution(graph, Role.generator)

    def test_edges_exist(self):
        """Tests that solutions that arent complete bicliques are not allowed."""
        graph = UndirectedGraph(num_vertices=10, edges=[])
        sol = Solution(s_1={1}, s_2={2})
        with self.assertRaises(ValidationError):
            sol.validate_solution(graph, Role.generator)

    def test_edges_missing(self):
        """Asserts that solutions that aren't bipartite are not allowed."""
        graph = UndirectedGraph(num_vertices=10, edges=[(i, j) for i in range(10) for j in range(i)])
        sol = Solution(s_1={1, 2}, s_2={3, 4})
        with self.assertRaises(ValidationError):
            sol.validate_solution(graph, Role.generator)


if __name__ == "__main__":
    unittest.main()
