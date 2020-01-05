# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


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
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('done')