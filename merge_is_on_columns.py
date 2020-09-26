# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['line_1', 'line_3', 'line_2'], columns= ['col_1', 'col_3', 'col_2']
    )
    new_data = data[['col_2', 'col_3', 'col_1']]
    return


if __name__ == '__main__':
    main()
    print('main - done')