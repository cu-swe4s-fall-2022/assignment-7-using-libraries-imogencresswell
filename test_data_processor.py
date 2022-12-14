"""Tests the functions in data_processor using unittest
"""
import sys
import os
import unittest
import csv
import shutil
import random
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.num_rows = random.choice(range(1, 10))
        self.num_cols = random.choice(range(1, 10))
        vals = [0] * self.num_rows
        for x in range(self.num_rows):
            vals[x] = [0] * self.num_cols
        with open('test_data.csv', 'w') as f:
            writer = csv.writer(f)

            writer.writerows(vals)
        self.testdata = 'test_data.csv'

    def test_get_random_matrix(self):
        self.assertTrue(data_processor.get_random_matrix(
            self.num_rows, self.num_cols).shape == (self.num_rows,
                                                    self.num_cols))
        self.assertFalse(data_processor.get_random_matrix(
            self.num_rows, self.num_cols).shape == (11, 11))
        self.assertRaises(
            TypeError, data_processor.get_random_matrix, 5.1, 6.8)
        self.assertRaises(ValueError, data_processor.get_random_matrix, -1, 1)

    def test_get_file_dimensions(self):
        self.assertTrue(data_processor.get_file_dimensions(
            self.testdata) == (self.num_rows, self.num_cols))
        self.assertFalse(data_processor.get_file_dimensions(
            self.testdata) == (11, 11))
        self.assertRaises(FileNotFoundError,
                          data_processor.get_file_dimensions, 'trial.csv')

    def test_write_matrix_to_file(self):
        data_processor.write_matrix_to_file(
            self.num_rows, self.num_cols, 'writetest.csv')
        self.assertTrue(data_processor.get_file_dimensions(
            'writetest.csv') == (self.num_rows, self.num_cols))
        self.assertFalse(data_processor.get_file_dimensions(
            'writetest.csv') == (11, 11))
        self.assertRaises(
            TypeError, data_processor.write_matrix_to_file, 5.1,
            6.8, 'intcheck.csv')
        self.assertRaises(
            ValueError, data_processor.write_matrix_to_file,
            -1, 1, 'zerocheck.csv')

    def tearDown(self):
        os.remove(self.testdata)


if __name__ == "__main__":
    unittest.main()
