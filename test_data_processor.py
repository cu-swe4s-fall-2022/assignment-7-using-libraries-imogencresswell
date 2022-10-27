"""Tests the functions in utils using unittest
"""
import sys
import os
import unittest
import numpy as np
import shutil
import random
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    def test_get_random_matrix(self):
        self.assertTrue(data_processor.get_random_matrix(self.num_rows, self.num_cols) = (num_rows, num_cols))
        self.assertFalse(data_processor.get_random_matrix(self.num_rows, self.num_cols) = (11, 11))
        self.assertRaises(TypeError, data_processor.get_random_matrix(5.1,6.8))

    def test_get_file_dimensions(self):
        self.assertTrue(data_processor.test_file_dimensions(self.testdata) = (num_rows, num_cols))
        self.assertFalse(data_processor.test_file_dimensions(self.testdata) = (11, 11))
        self.assertRaises(FileNotFoundError, data_processor.test_file_dimensions(self.testdata))
    
    def test_write_matrix_to_file(self):
        data_processor.write_matrix_to_file(self.num_rows, self.num_cols, 'writetest.csv')
        self.assertTrue(data_processor.get_file_dimensions('writetest.csv') = (num_rows, num_cols))
        self.assertFalse(data_processor.get_file_dimensions('writetest.csv') = (11, 11))
        self.assertRaises(TypeError, data_processor.write_matrix_to_file(5.1,6.8, 'intcheck.csv'))
    def setUp(self):
        self.num_rows = random.choice(range(0,10))
        self.num_cols = random.choice(range(0,10))
        self.rand_arr = np.empty((self.num_rows, self.num_cols))
        np.savetxt('testdata.csv',self.rand_arr, delimiter=',')
        self.testdata = 'testdata.csv')

    def tearDown(self):
        os.remove('./testdata.csv')
        

if __name__ == "__main__":
    unittest.main()
