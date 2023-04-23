"""Tests for the Pathpacking problem."""
import unittest
import logging

from algobattle_problems.pathpacking import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the Pathpacking parser."""

    def setUp(self) -> None:
        self.parser = parser.PathpackingParser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('e', '1', '2'), ('e', '3', '2'), ('s', '1', '2', '9'), ('s', '5', '6', '7'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('e', '1', '2'), ('e', '3', '2')], [('s', '1', '2', '9'), ('s', '5', '6', '7')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('e', '1', '2', '1'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('e', '1'), ('e')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_large_labels(self):
        raw_instance = [('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_duplicates(self):
        raw_instance = [('e', '3', '2'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_letter_lines(self):
        raw_instance = [('e', '3', 'a'), ('e', 'b', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_zero_label(self):
        raw_instance = [('e', '1', '0'), ('e', '0', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_selfloop(self):
        raw_instance = [('e', '1', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('s', '1', '2', '9', '10'), ('s', '5', '6', '7')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('s', '5', '6', '7')])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('s', '1', '2', '9'), ('s', '5', '6')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('s', '1', '2', '9')])

    def test_parse_solution_too_large_labels(self):
        raw_solution = [('s', '1', '2', '11'), ('s', '1', '2', '9')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=9), [('s', '1', '2', '9')])

    def test_parse_solution_letter_labels(self):
        raw_solution = [('s', '1', 'a', '9'), ('s', '3', '2', '9')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('s', '3', '2', '9')])

    def test_parse_solution_zero_labels(self):
        raw_solution = [('s', '0', '2', '9'), ('s', '5', '6', '7')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('s', '5', '6', '7')])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=2), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('e', '1', '2'), ('e', '3', '2'), ('s', '1', '2', '9'), ('s', '5', '6', '7')]),
                         """e 1 2\ne 3 2\ns 1 2 9\ns 5 6 7""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode("""e 1 2\ne 3 2\ns 1 2 9\ns 5 6 7""".encode()),
                         [('e', '1', '2'), ('e', '3', '2'), ('s', '1', '2', '9'), ('s', '5', '6', '7')])


class Verifiertests(unittest.TestCase):
    """Tests for the Pathpacking verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.PathpackingVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('e', '1', '2'),
                                                                    ('e', '3', '1'), ('e', '3', '2')], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_semantics_of_solution_wrong_path_length(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([('s', '1', '2', '1')], 10, solution_type=False))

    def test_verify_semantics_of_solution_correct_path_length(self):
        self.assertTrue(self.verifier.verify_semantics_of_solution([('s', '1', '2', '3')], 10, solution_type=False))

    def test_verify_solution_against_instance_one_path(self):
        instance = [('e', '1', '2'), ('e', '3', '1'), ('e', '3', '2'), ('e', '2', '4'),
                    ('e', '3', '4'), ('e', '4', '5'), ('e', '4', '6')]
        solution = [('s', '1', '2', '3')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_two_paths(self):
        instance = [('e', '1', '2'), ('e', '3', '1'), ('e', '3', '2'), ('e', '2', '4'),
                    ('e', '3', '4'), ('e', '4', '5'), ('e', '4', '6')]
        solution = [('s', '1', '2', '3'), ('s', '5', '4', '6')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_invalid(self):
        instance = [('e', '1', '2'), ('e', '3', '1'), ('e', '3', '2'), ('e', '2', '4'),
                    ('e', '3', '4'), ('e', '4', '5'), ('e', '4', '6')]
        solution = [('s', '1', '4', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_equal_solution_size(self):
        instance = [('e', '1', '2'), ('e', '3', '1'), ('e', '3', '2'), ('e', '2', '4'),
                    ('e', '3', '4'), ('e', '4', '5'), ('e', '4', '6'), ('e', '6', '7')]
        solution1 = [('s', '1', '2', '3'), ('s', '5', '4', '6')]
        solution2 = [('s', '1', '2', '3'), ('s', '4', '6', '7')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution1, instance_size=10, solution_type=False))
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution2, instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio(self):
        instance = [('e', '1', '2'), ('e', '3', '1'), ('e', '3', '2'), ('e', '2', '4'),
                    ('e', '3', '4'), ('e', '4', '5'), ('e', '4', '6'), ('e', '6', '7')]
        solution_sufficient = [('s', '1', '2', '3'), ('s', '5', '4', '6')]
        solution_too_little = [('s', '1', '2', '3')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_too_little), 2.0)
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_sufficient), 1.0)


if __name__ == '__main__':
    unittest.main()
