# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    data_without_column_or_row_names = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]
    )
    # both axis have {RangeIndex: 3}
    # lists are rows
    data_with_column_names = pd.DataFrame(
        {'a': [1, 2, 3],
         'b': [4, 5, 6],
         'c': [7, 8, 9]}
    )
    # column names and list as columns
    data_with_row_names = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c']
    )
    # row names added after creation
    data_with_row_and_column_names = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c'], columns= [10, 11, 12]
    )
    # numbers as column names
    data_with_nested_dict = pd.DataFrame(
        {'first_column': {'first_row': 1, 'second_row': 2, 'third_row':3},
         'second_column': {'first_row': 4, 'second_row': 5, 'third_row':6},
         'third_column': {'first_row': 7, 'second_row': 8, 'third_row':9},}
    )
    numpy_from_nested_lists = np.array(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]
    )
    # inner lists are rows
    pd_data = pd.DataFrame(numpy_from_nested_lists)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('done')