"""Tests for the Pairsum problem."""
import unittest
import logging

from problems.pairsum import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the Pairsum Parser."""

    def setUp(self) -> None:
        self.parser = parser.PairsumParser()

    def test_split_into_instance_and_solution(self):
        raw_input = ['1 2 3 4', '0 3 1 2']
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ('1 2 3 4', ['0 3 1 2']))

        # empty inputs should be handled
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ('', ['']))

        # Input of wrong length are discarded
        self.assertEqual(self.parser.split_into_instance_and_solution(['1', '2', '3']), ('', ['']))

    def test_parse_instance_ints(self):
        # Entries should be ints
        raw_instance = '1 2 3 4 a'
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=10), [1, 2, 3, 4])

    def test_parse_instance_too_short(self):
        # Entries should be ints
        raw_instance = '1 2 3'
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=10), [])

    def test_parse_instance_negative(self):
        raw_instance = '1 7 3 4 -10'
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=10), [1, 7, 3, 4])

    def test_parse_instance_huge_entry(self):
        # entries should not exceed 2**63
        raw_instance = '1 2 3 4 {}'.format(2**64)
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=10), [1, 2, 3, 4])

    def test_parse_instance_prune(self):
        # Instance should be cut down to instance_size number of entries
        raw_instance = '1 2 3 4 5 6'
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=5), [1, 2, 3, 4, 5])

    def test_parse_instance_empty(self):
        # empty inputs should be handled
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_ints(self):
        # Entries should be ints
        raw_solution = ['0 3 1 2 a']
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [0, 3, 1, 2])

    def test_parse_solution_size(self):
        # Entries should not exceed instance_size
        raw_solution = ['0 3 1 2 4']
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [0, 3, 1, 2])

    def test_encode(self):
        self.assertEqual(self.parser.encode(['1 2 3 4']),
                         """1 2 3 4""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode(
                         """1 2 3 4\n0 3 1 2""".encode()), ['1 2 3 4', '0 3 1 2'])


class Verifiertests(unittest.TestCase):
    """Tests for the Pairsum Verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.PairsumVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([1, 2, 3, 4], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_semantics_of_solution_too_short(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([0, 3, 1], 10, solution_type=False))

    def test_verify_semantics_of_solution_duplicates(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([0, 3, 1, 1], 10, solution_type=False))

    def test_verify_semantics_of_solution_normal(self):
        self.assertTrue(self.verifier.verify_semantics_of_solution([0, 3, 1, 2], 10, solution_type=False))

    def test_verify_solution_against_instance_normal(self):
        # Valid solutions should be accepted
        instance = [1, 2, 3, 4]
        solution = [0, 3, 1, 2]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_wrong(self):
        # Invalid solutions should not be accepted
        instance = [1, 2, 3, 4]
        solution = [0, 1, 2, 3]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio(self):
        instance = [1, 2, 3, 4]
        solution = [0, 1, 2, 3]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance, 10, solution, solution), 1.0)


if __name__ == '__main__':
    unittest.main()
