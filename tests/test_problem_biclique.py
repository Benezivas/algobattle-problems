"""Tests for the biclique problem."""
import unittest
import logging

from problems.biclique import Problem

logging.disable(logging.CRITICAL)


class SolutionTests(unittest.TestCase):
    """Tests for the Biclique problem solution class."""
    
    def test_vertices_exist(self):
        """Tests that only valid vertex indices are allowed."""
        graph = Problem(num_vertices=10, edges=[(i, j) for i in range(10) for j in range(i)])
        sol = Problem.Solution(s_1=set(), s_2={20})
        self.assertFalse(sol.is_valid(graph, 10))

    def test_edges_exist(self):
        """Tests that solutions that arent complete bicliques are not allowed."""
        graph = Problem(num_vertices=10, edges=[])
        sol = Problem.Solution(s_1={1}, s_2={2})
        self.assertFalse(sol.is_valid(graph, 10))

    def test_edges_missing(self):
        """Asserts that solutions that aren't bipartite are not allowed."""
        graph = Problem(num_vertices=10, edges=[(i, j) for i in range(10) for j in range(i)])
        sol = Problem.Solution(s_1={1, 2}, s_2={3, 4})
        self.assertFalse(sol.is_valid(graph, 10))


if __name__ == '__main__':
    unittest.main()
