"""Tests for the OSCM3 problem."""
import unittest

from algobattle_problems.oscm3.problem import OSCM3, ValidationError


class OSCM3Tests(unittest.TestCase):
    """Tests for the OSCM3 verifier."""

    @classmethod
    def setUpCls(cls) -> None:
        cls.instance = OSCM3(size=3, neighbors={
            0: {1, 2},
            1: {0, 1, 2},
            2: {0, 1},
        })

    def test_too_many_neighbors(self):
        with self.assertRaises(ValidationError):
            instance = OSCM3(size=4, neighbors={0: {0, 1, 2, 3}})
            instance.validate_instance(4)
    
    def test_solution_not_permutation(self):
        with self.assertRaises(ValidationError):
            OSCM3.Solution(vertex_order=[0, 0, 0]).validate_solution(self.instance)

    def test_solution_too_small(self):
        with self.assertRaises(ValidationError):
            OSCM3.Solution(vertex_order=[0, 1]).validate_solution(self.instance)

    def test_solution_wrong_indices(self):
        with self.assertRaises(ValidationError):
            OSCM3.Solution(vertex_order=[1, 2, 3]).validate_solution(self.instance)


if __name__ == '__main__':
    unittest.main()
