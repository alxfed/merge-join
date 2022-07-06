# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    data = pd.DataFrame(
        [[1, '###', 3],
         [4, 5, 6],
         ['###', 8, 0],
         [1, 2, 3]], index=['line_1', 'line_3', 'line_2', 'line_4'], columns= ['col_1', 'col_3', 'col_2']
    )

    cols = pd.Index(['col_1', 'col_2', 'col_3'], dtype=str, name='columns')
    inde = pd.Index(['line_1', 'line_2', 'line_3', 'line_4'], dtype=str, name='lines')
    result = data.reindex(index=inde, columns=cols)
    #
    # no_duplicates = data.drop_duplicates(subset=['col_1', 'col_2'], keep='last', inplace=False, ignore_index=False)
    # index_of_not_dropped = no_duplicates.index
    # dropped = data.drop(index=index_of_not_dropped)

    a = data.replace(to_replace='###', value='X', inplace=True)

    m = (data != '###')
    result = data.where(m, None).dropna()

    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')