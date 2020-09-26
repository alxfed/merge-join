# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data2 = pd.DataFrame(
        {'a': [1, 2, 3],
         'b': [4, 5, 6],
         'c': [7, 8, 9]}
    )
    data_stacked = data2.stack()
    data_concat = pd.concat([data2['a'], data2['b']])
    data_plus = data2.pivot_table()
    print('ok')

if __name__ == '__main__':
    main()
    print('\ndone')