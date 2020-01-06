# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def row_processor(row):
    a = row['c2']
    return a


def main():
    data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c'], columns= ['c1', 'c2', 'c3']
    )
    result = data.assign(added1 = lambda x: x['c1'] * 2,
                         added2 = lambda x: x['added1'] / 2)

    another = data.assign(added1 = lambda x: x.c1 * 2,
                          added2 = lambda x: x.added1 / 2)

    yet_another = data.assign(c4 = row_processor)

    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')