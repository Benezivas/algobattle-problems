"""Tests for the clusterediting problem."""
import unittest
import logging

from problems.clusterediting import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the clusterediting parser."""

    def setUp(self) -> None:
        self.parser = parser.ClustereditingParser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('e', '1', '2'), ('e', '3', '2'), ('s', 'add', '3', '1'), ('s', 'del', '1', '2'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('e', '1', '2'), ('e', '3', '2')], [('s', 'add', '3', '1'), ('s', 'del', '1', '2')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('e', '1', '2', '1'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('e', '1'), ('e')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_too_large_labels(self):
        raw_instance = [('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_duplicates(self):
        raw_instance = [('e', '3', '2'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_letter_entries(self):
        raw_instance = [('e', '3', 'a'), ('e', 'b', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_too_zero_labels(self):
        raw_instance = [('e', '1', '0'), ('e', '0', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_selfloop(self):
        raw_instance = [('e', '1', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('s', 'add', '3', '1', '5')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('s', 'add', '5')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_too_large_labels(self):
        raw_solution = [('s', 'add', '3', '10')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=9), [])

    def test_parse_solution_letter_entries(self):
        raw_solution = [('s', 'add', '3', 'foo')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_zero_label(self):
        raw_solution = [('s', 'add', '0', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=2), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('e', '1', '2'), ('e', '3', '2'), ('s', 'add', '1', '3')]),
                         """e 1 2\ne 3 2\ns add 1 3""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode("""e 1 2\ne 3 2\ns add 1 3""".encode()),
                         [('e', '1', '2'), ('e', '3', '2'), ('s', 'add', '1', '3')])


class Verifiertests(unittest.TestCase):
    """Tests for the clusterediting verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.ClustereditingVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('e', '1', '2')], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_solution(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_solution_against_instance_delete_nonexisting_edge(self):
        instance = [('e', '1', '2')]
        solution = [('s', 'del', '1', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_delete_extra_edge(self):
        instance = [('e', '1', '2'), ('e', '3', '2'), ('e', '1', '3'), ('e', '1', '4')]
        solution = [('s', 'del', '1', '4')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_delete_and_add_edge(self):
        instance = [('e', '1', '2'), ('e', '3', '2'), ('e', '1', '4')]
        solution = [('s', 'add', '1', '3'), ('s', 'del', '1', '4')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_delete_and_add_edges(self):
        instance = [('e', '1', '3'), ('e', '1', '5'), ('e', '1', '9'), ('e', '2', '6'), ('e', '2', '8'),
                    ('e', '2', '9'), ('e', '3', '4'), ('e', '3', '6'), ('e', '3', '7'), ('e', '4', '7'), ('e', '5', '9')]
        solution = [('s', 'del', '2', '9'), ('s', 'del', '1', '3'), ('s', 'del', '3', '6'), ('s', 'add', '6', '8')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_delete_edge_invalid(self):
        instance = [('e', '1', '2'), ('e', '3', '2'), ('e', '1', '3')]
        solution = [('s', 'del', '1', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_add_edge_invalid(self):
        instance = [('e', '1', '2'), ('e', '3', '2'), ('e', '1', '3'), ('e', '1', '4')]
        solution = [('s', 'add', '3', '4')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_delete_and_add_invalid_edge(self):
        instance = [('e', '1', '2'), ('e', '3', '2'), ('e', '1', '3'), ('e', '1', '4')]
        solution = [('s', 'add', '3', '4'), ('s', 'del', '1', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio(self):
        instance = [('e', '1', '2'), ('e', '1', '3'), ('e', '1', '4'), ('e', '2', '3'),
                    ('e', '2', '4'), ('e', '3', '4'), ('e', '1', '5')]
        solution_sufficient = [('s', 'del', '1', '5')]
        solution_too_much = [('s', 'del', '1', '5'), ('s', 'del', '4', '1'), ('s', 'del', '4', '2'), ('s', 'del', '4', '3')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_too_much), 4.0)
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance,
                                                                     10, solution_sufficient, solution_sufficient), 1.0)


if __name__ == '__main__':
    unittest.main()
