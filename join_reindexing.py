# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data_with_column_names = pd.DataFrame(
        {'a': [1, 2, 3],
         'b': [4, 5, 6],
         'c': [7, 8, 9]}
    )
    data = data_with_column_names.set_index(keys='a', drop=False, verify_integrity=False)
    re_data = data.reindex(index=[3, 2, 1], columns=['c', 'b', 'a'])
    print(re_data)
    return


if __name__ == '__main__':
    main()
    print('main - done')