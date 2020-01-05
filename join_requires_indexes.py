# -*- coding: utf-8 -*-
"""https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
"""
import pandas as pd


def main():
    data_with_column_names = pd.DataFrame(
        {'a': [1, 2, 3],
         'b': [4, 5, 6],
         'c': [7, 8, 9]}
    )
    data = data_with_column_names.set_index(keys='a', drop=False, verify_integrity=False)
    # drop means delete the column used for index creation
    old_data = data.reset_index(drop=True)
    # back to the initial state
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')