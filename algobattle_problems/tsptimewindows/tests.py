"""Tests for the scheduling problem."""
import unittest

from pydantic import ValidationError as PydanticValidationError

from algobattle_problems.tsptimewindows.problem import (
    Instance,
    Solution,
    ValidationError,
    Location,
    Role,
    Tsptimewindows
)


class Tests(unittest.TestCase):
    """Tests for the Tsp with timewindows problem."""

    @classmethod
    def setUpClass(cls):
        cls.instance = Instance(
            locations=[
                Location(x=0, y=0, min_time=0, max_time=3),
                Location(x=1, y=0, min_time=1, max_time=2),
            ]
        )
        cls.instance_short = Instance(
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
        node_tour = list(Solution(tour=tour).location_tour(self.instance))
        self.assertEqual(node_tour, nodes)

    def test_tour_too_short(self):
        with self.assertRaises(PydanticValidationError):
            Solution.model_validate({"tour": []}, context={"instance": self.instance})

    def test_duplicate_in_tour(self):
        with self.assertRaises(PydanticValidationError):
            Solution.model_validate({"tour": [0, 0]}, context={"instance": self.instance})

    def test_tour_wrong_index(self):
        with self.assertRaises(PydanticValidationError):
            Solution.model_validate({"tour": [10, 10]}, context={"instance": self.instance})

    def test_tour_too_slow(self):
        with self.assertRaises(ValidationError):
            sol = Solution.model_validate({"tour": [1, 0]}, context={"instance": self.instance})
            sol.validate_solution(self.instance, Role.generator)

    def test_gen_tour_wrong(self):
        solution = Solution(tour=[0, 1])
        solution.score(self.instance_short, Role.solver)
        with self.assertRaises(ValidationError):
            solution.validate_solution(self.instance_short, Role.generator)

    def test_score_gen_wrong(self):
        solution = Solution(tour=[0, 1])
        with self.assertRaises(ValidationError):
            Tsptimewindows.score(self.instance_short, generator_solution=solution, solver_solution=solution)


if __name__ == "__main__":
    unittest.main()
