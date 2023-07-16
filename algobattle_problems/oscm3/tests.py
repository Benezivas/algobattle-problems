"""Tests for the OSCM3 problem."""
import unittest

from algobattle_problems.oscm3.problem import Instance, Solution, ValidationError, Role


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
            instance = Instance(neighbors={0: {0, 1, 2, 3}, 3: set()})
            instance.validate_instance()

    def test_solution_not_permutation(self):
        with self.assertRaises(ValidationError):
            Solution(vertex_order=[0, 0, 0]).validate_solution(self.instance, Role.generator)

    def test_solution_too_small(self):
        with self.assertRaises(ValidationError):
            Solution(vertex_order=[0, 1]).validate_solution(self.instance, Role.generator)

    def test_solution_wrong_indices(self):
        with self.assertRaises(ValidationError):
            Solution(vertex_order=[1, 2, 3]).validate_solution(self.instance, Role.generator)


if __name__ == "__main__":
    unittest.main()
