"""Tests for the OSCM3 problem."""
import unittest
import logging

from algobattle_problems.oscm3 import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the OSCM3 Parser."""

    def setUp(self) -> None:
        self.parser = parser.OSCM3Parser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'),
                     ('n', '2', '0', '1'), ('s', '0', '1', '2'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1')], [('s', '0', '1', '2')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1', '0', '0')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2')]))

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('n', '0'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1', '0', '0')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0'), ('n', '1', '0', '1', '2'), ('n', '2')]))

    def test_parse_instance_too_large_labels(self):
        raw_instance = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1'), ('n', '3', '2')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1')]))

    def test_parse_instance_too_many_entries_more(self):
        raw_instance = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '3', '1')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2')]))

    def test_parse_instance_duplicates(self):
        raw_instance = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1'), ('n', '2', '0', '1')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1')]))

    def test_parse_instance_letter_labels(self):
        raw_instance = [('n', '0', '1', '2'), ('n', 'a', '0', '1', '2'), ('n', '2', 'a', '1')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1'), ('n', '2')]))

    def test_parse_instance_multi_edges(self):
        raw_instance = [('n', '0', '1', '2'), ('n', '1', '1', '1', '2'), ('n', '2', '0', '1')]
        self.assertEqual(set(self.parser.parse_instance(raw_instance, instance_size=3)),
                         set([('n', '0', '1', '2'), ('n', '1'), ('n', '2', '0', '1')]))

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [('n', '0'), ('n', '1'), ('n', '2')])

    def test_parse_solution_multiple_solutions(self):
        raw_solution = [('s', '0', '1', '2'), ('s', '2', '1', '0')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), ('s', '0', '1', '2'))

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('s', '0', '1', '2', '3')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('s', '0', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [])

    def test_parse_solution_too_large_labels(self):
        raw_solution = [('s', '10', '1', '2')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [])

    def test_parse_solution_letter_labels(self):
        raw_solution = [('s', 'a', '1', '2')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [])

    def test_parse_solution_duplicate_nodes(self):
        raw_solution = [('s', '0', '2', '2')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=3), [])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=3), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('n', '0', '1', '2'), ('n', '1', '0', '1', '2'),
                                             ('n', '2', '0', '1'), ('s', '0', '1', '2')]),
                         """n 0 1 2\nn 1 0 1 2\nn 2 0 1\ns 0 1 2""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode("""n 0 1 2\nn 1 0 1 2\nn 2 0 1\ns 0 1 2""".encode()),
                         [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1'), ('s', '0', '1', '2')])


class Verifiertests(unittest.TestCase):
    """Tests for the OSCM3 verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.OSCM3Verifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('n', '0', '1', '2')], instance_size=2))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=2))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 2, solution_type=False))

    def test_verify_semantics_of_solution(self):
        self.assertTrue(self.verifier.verify_semantics_of_solution(('s', '0', '1'), 2, solution_type=False))

    def test_verify_solution_against_instance(self):
        instance = [('n', '0', '1', '2')]
        solution = ('s', '0', '1')
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=2, solution_type=False))

    def test_calculate_approximation_ratio_diff_sizes(self):
        instance = [('n', '0', '1', '2'), ('n', '1', '0', '1', '2'), ('n', '2', '0', '1')]
        solution_sufficient = ('s', '2', '1', '0')
        solution_too_little = ('s', '0', '1', '2')
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     3, solution_sufficient, solution_too_little), 9 / 2)
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     3, solution_sufficient, solution_sufficient), 1.0)

    def test_calculate_approximation_ratio_diff_crossings(self):
        instance = [('n', '0', '0'), ('n', '1', '1')]
        solution_no_crossings = ('s', '0', '1')
        solution_one_crossing = ('s', '1', '0')
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     2, solution_no_crossings, solution_no_crossings), 1.0)
        self.assertGreater(self.verifier.calculate_approximation_ratio(instance,
                                                                       2, solution_no_crossings, solution_one_crossing), 1.0)


if __name__ == '__main__':
    unittest.main()
