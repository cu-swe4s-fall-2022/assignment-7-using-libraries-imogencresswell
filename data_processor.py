import pandas as pd
import numpy as np
def get_random_matrix(num_rows, num_columns):
    if type(num_rows) != int or type(num_columns) != int:
        raise TypeError('Rows and cols must be int')
    elif num_rows < 0 or num_columns < 0:
        raise ValueError('Rows and cols must be positive')
    else:
        return np.random.rand(num_rows, num_columns)

def get_file_dimensions(file_name):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find' + file_name)
        
	    
    readfile = pd.read_csv(file_name, header=None)
    rows = len(readfile)
    cols = len(readfile.columns)

    return (rows,cols)

def write_matrix_to_file(num_rows, num_columns, file_name):
    matrix = get_random_matrix(num_rows, num_columns)
    np.savetxt(str(file_name), matrix, delimiter=',')
