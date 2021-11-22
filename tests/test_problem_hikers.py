"""Tests for the hikers problem."""
import unittest
import logging

from problems.hikers import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the hikers parser."""

    def setUp(self) -> None:
        self.parser = parser.HikersParser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('h', '1', '1', '3'), ('h', '2', '10', '12'), ('h', '3', '1', '1'), ('h', '4', '2', '5'),
                     ('h', '5', '3', '3'), ('s', '3', '1'), ('s', '1', '2'), ('s', '4', '2'), ('s', '5', '2'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('h', '1', '1', '3'), ('h', '2', '10', '12'), ('h', '3', '1', '1'),
                           ('h', '4', '2', '5'), ('h', '5', '3', '3')],
                          [('s', '3', '1'), ('s', '1', '2'), ('s', '4', '2'), ('s', '5', '2')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('h', '1', '1', '3', '4'), ('h', '2', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '2', '10', '12')])

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('h', '3', '4'), ('h', '2', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '2', '10', '12')])

    def test_parse_instance_too_large_labels(self):
        raw_instance = [('h', '1', '1', '3'), ('h', '3', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [('h', '1', '1', '3')])

    def test_parse_instance_duplicates(self):
        raw_instance = [('h', '3', '10', '12'), ('h', '3', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '3', '10', '12')])

    def test_parse_instance_letter_labels(self):
        raw_instance = [('h', '3', '10', '12'), ('h', 'a', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '3', '10', '12')])

    def test_parse_instance_zero_label(self):
        raw_instance = [('h', '0', '1', '3'), ('h', '3', '10', '12')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '3', '10', '12')])

    def test_parse_instance_empty_pref_interval(self):
        raw_instance = [('h', '3', '12', '10'), ('h', '1', '1', '3')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '1', '1', '3')])

    def test_parse_instance_dupliacte_hiker(self):
        raw_instance = [('h', '1', '10', '12'), ('h', '1', '1', '3')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=20), [('h', '1', '10', '12')])

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('s', '3', '1', '5')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('s', '3')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_too_large_labels(self):
        raw_solution = [('s', '11', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=9), [])

    def test_parse_solution_letter_labels(self):
        raw_solution = [('s', 'a', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_zero_labels(self):
        raw_solution = [('s', '0', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=2), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('h', '1', '1', '3'), ('h', '2', '10', '12'), ('h', '3', '1', '1'),
                                             ('h', '4', '2', '5'), ('h', '5', '3', '3'), ('s', '3', '1')]),
                         """h 1 1 3\nh 2 10 12\nh 3 1 1\nh 4 2 5\nh 5 3 3\ns 3 1""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode(
                         """h 1 1 3\nh 2 10 12\nh 3 1 1\nh 4 2 5\nh 5 3 3\ns 3 1""".encode()),
                         [('h', '1', '1', '3'), ('h', '2', '10', '12'), ('h', '3', '1', '1'),
                         ('h', '4', '2', '5'), ('h', '5', '3', '3'), ('s', '3', '1')])


class Verifiertests(unittest.TestCase):
    """Tests for the hikers verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.HikersVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('h', '1', '1', '3')], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_semantics_of_solution(self):
        self.assertTrue(self.verifier.verify_semantics_of_solution([('s', '5', '2')], 10, solution_type=False))

    def test_verify_solution_against_instance_valid(self):
        instance = [('h', '1', '1', '3'), ('h', '2', '10', '12'),
                    ('h', '3', '1', '1'), ('h', '4', '2', '5'), ('h', '5', '3', '3')]
        solution = [('s', '3', '1'), ('s', '1', '2'), ('s', '4', '2'), ('s', '5', '2')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_invalid_single(self):
        instance = [('h', '4', '2', '5')]
        solution = [('s', '4', '1')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_valid_double(self):
        instance = [('h', '1', '1', '3'), ('h', '3', '1', '1')]
        solution = [('s', '1', '1'), ('s', '3', '1')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio(self):
        instance = [('h', '1', '1', '3'), ('h', '2', '10', '12'), ('h', '3', '1', '1'),
                    ('h', '4', '2', '5'), ('h', '5', '3', '3'), ('h', '6', '1', '1')]
        solution_sufficient = [('s', '3', '1'), ('s', '1', '2'), ('s', '4', '2'), ('s', '5', '2'), ('s', '6', '3')]
        solution_too_little = [('s', '3', '1'), ('s', '1', '2'), ('s', '4', '2'), ('s', '5', '2')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_too_little), 5 / 4)
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_sufficient), 1.0)


if __name__ == '__main__':
    unittest.main()
