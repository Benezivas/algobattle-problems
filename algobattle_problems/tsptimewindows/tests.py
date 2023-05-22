"""Tests for the scheduling problem."""
import unittest

from algobattle_problems.tsptimewindows.problem import Tsptimewindows, ValidationError, Location
from algobattle.util import Role


class Tests(unittest.TestCase):
    """Tests for the Tsp with timewindows problem."""

    @classmethod
    def setUpClass(cls):
        cls.instance = Tsptimewindows(
            locations=[
                Location(x=0, y=0, min_time=0, max_time=3),
                Location(x=1, y=0, min_time=1, max_time=2),
            ]
        )
        cls.instance_short = Tsptimewindows(
            locations=[
                Location(x=0, y=0, min_time=0, max_time=3),
                Location(x=1.05, y=0, min_time=0, max_time=1),
            ]
        )

    def test_node_tour(self):
        tour = [0, 1]
        nodes = [
            self.instance.locations[0],
            self.instance.locations[1],
            self.instance.locations[0],
        ]
        node_tour = list(Tsptimewindows.Solution(tour=tour).location_tour(self.instance))
        self.assertEqual(node_tour, nodes)

    def test_tour_too_short(self):
        with self.assertRaises(ValidationError):
            Tsptimewindows.Solution(tour=[]).validate_solution(self.instance)

    def test_duplicate_in_tour(self):
        with self.assertRaises(ValidationError):
            Tsptimewindows.Solution(tour=[0, 0]).validate_solution(self.instance)

    def test_tour_wrong_index(self):
        with self.assertRaises(ValidationError):
            Tsptimewindows.Solution(tour=[10, 10]).validate_solution(self.instance)

    def test_tour_too_slow(self):
        with self.assertRaises(ValidationError):
            Tsptimewindows.Solution(tour=[1, 0]).validate_solution(self.instance)

    def test_gen_tour_wrong(self):
        solution = Tsptimewindows.Solution(tour=[0, 1])
        solution.validate_solution(self.instance_short)
        solution.score(self.instance_short, Role.solver)
        with self.assertRaises(ValidationError):
            solution.score(self.instance_short, Role.generator)

    def test_score_gen_wrong(self):
        solution = Tsptimewindows.Solution(tour=[0, 1])
        self.assertEqual(self.instance_short.score(solution, solution), 0)


if __name__ == "__main__":
    unittest.main()
