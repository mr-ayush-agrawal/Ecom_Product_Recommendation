from math import ceil
from typing import List
import pandas as pd
import os

def display_grid(items : List, columns):
    num_columns = len(columns)
    num_rows = ceil(len(items) / num_columns)  # Calculate how many rows will be needed

    for row in range(num_rows):
        cols = columns  # Create the columns
        for i in range(num_columns):
            index = row * num_columns + i  # Get the correct index
            if index < len(items):
                cols[i].write(items[index])

def get_products_list() -> List:
    '''
    Returns the list of all the Product list presnt in the dataset
    '''
    path = os.path.join(os.getcwd(), 'Data/Processed_matrix.csv')
    df = pd.read_csv(path, index_col='UserId')
    cols_list = df.columns.tolist()

    return cols_list