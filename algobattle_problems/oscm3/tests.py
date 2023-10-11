"""Tests for the OSCM3 problem."""
import unittest

from pydantic import ValidationError

from algobattle_problems.oscm3.problem import Instance, Solution


class Tests(unittest.TestCase):
    """Tests for the OSCM3 verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Instance(
            neighbors={
                0: {1, 2},
                1: {0, 1, 2},
                2: {0, 1},
            }
        )

    def test_too_many_neighbors(self):
        with self.assertRaises(ValidationError):
            Solution.model_validate({"neighbors": {0: {0, 1, 2, 3}, 3: set()}})

    def test_solution_not_permutation(self):
        with self.assertRaises(ValidationError):
            Solution.model_validate({"vertex_order": [0, 0, 0]}, context={"instance": self.instance})

    def test_solution_too_small(self):
        with self.assertRaises(ValidationError):
            Solution.model_validate({"vertex_order": [0, 1]}, context={"instance": self.instance})

    def test_solution_wrong_indices(self):
        with self.assertRaises(ValidationError):
            Solution.model_validate({"vertex_order": [1, 2, 3]}, context={"instance": self.instance})


if __name__ == "__main__":
    unittest.main()
