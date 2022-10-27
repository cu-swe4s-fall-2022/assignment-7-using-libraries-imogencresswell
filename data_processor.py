"""
Functions for homework 7
-get_random_matrix - creates an NxM matrix of random numbers
-get_file_dimensions - returns number of rows x number of columns
                       for given file
-write_matrix_to_file - creates random NxM matrix and writes to
                        CSV file
"""

import pandas as pd
import numpy as np


def get_random_matrix(num_rows, num_columns):
    """Returns a random matrix of N rowx x M columns
    Parameters
    ----------
    num rows : integer
        Number of rows
    num columns : integer
        Number of columns
    Returns
    -------
    num_rows x num_columns matrix

    """
    if type(num_rows) != int or type(num_columns) != int:
        raise TypeError('Rows and cols must be int')
    elif num_rows < 0 or num_columns < 0:
        raise ValueError('Rows and cols must be positive')
    else:
        return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):
    """Finds dimensions of given file
    Parameters
    ----------
    file_name  : string
        Name of file to search
    Returns
    -------
    Tuple containing no. of rows and no. of columns

    """
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find' + file_name)

    readfile = pd.read_csv(file_name, header=None)
    rows = len(readfile)
    cols = len(readfile.columns)

    return (rows, cols)


def write_matrix_to_file(num_rows, num_columns, file_name):
    """Writes a random matrix of N rowx x M columns to file
    Parameters
    ----------
    num rows : integer
        Number of rows
    num columns : integer
        Number of columns
    file_name: string
        Name of saved file
    Returns
    -------
    CSV file containing random matrix

    """
    matrix = get_random_matrix(num_rows, num_columns)
    np.savetxt(str(file_name), matrix, delimiter=',')
