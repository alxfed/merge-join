# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data_1 = pd.DataFrame(
        [[1, 2, 3, 1],
         [4, 5, 6, 2],
         [7, 8, 0, 3]], index=['line_1', 'line_3', 'line_2'], columns= ['date', 'day_n', 'tagg', 'sum_total']
    )
    data_2 = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['line_1', 'line_3', 'line_2'], columns= ['col_1', 'col_3', 'col_2']
    )
    return


if __name__ == '__main__':
    main()
    print('main - done')