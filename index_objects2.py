# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    data_with_row_and_column_names = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=[0, 2, 1], columns= ['col_1', 'col_3', 'col_2']
    )

    cols = pd.Index(['col_1', 'col_2', 'col_3'], dtype=str, name='columns')
    inde = pd.Index([0, 1, 2], dtype=int, name='lines')
    result = data_with_row_and_column_names.reindex(index=inde, columns=cols)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')