# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    data_with_row_and_column_names = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['line_1', 'line_3', 'line_2'], columns= ['col_1', 'col_3', 'col_2']
    )

    cols = pd.Index(['col_1', 'col_2', 'col_3'], dtype=str, name='columns')
    inde = pd.Index(['line_1', 'line_2', 'line_3'], dtype=str, name='lines')
    result = data_with_row_and_column_names.reindex(index=inde, columns=cols)
    a = pd.DataFrame()
    a['col_1'] = result.col_1
    print('ok')
    return


def another_main():
    indx = pd.MultiIndex.from_tuples([('Parameters', 'time'),
                                      ('Parameters', 'price'),
                                      ('Weight', ''),
                                      ('Users', ''),
                                      ('Metrics', 'Retention_1 mean'),
                                      ('Metrics', 'Retention_1  sem'),
                                      ('Metrics', 'Retention_3 mean'),
                                      ('Metrics', 'Retention_3  sem'),
                                      ('Objective', 'Scalarized'),
                                      ('Objective', 'offline'),
                                      ('Tracking metrics', 'Conversion_0 mean'),
                                      ('Tracking metrics', 'Conversion_0  sem'),
                                      ('Tracking metrics', 'Conversion_1 mean'),
                                      ('Tracking metrics', 'Conversion_1  sem')])
    colm = pd.Index(['0_0', '0_1', '0_2', '0_3', '0_4', '0_5', 'status_quo'])
    it = pd.DataFrame(index=indx, columns=colm)
    it.style.set_properties(subset=['text'], **{'width': '300px'})
    return it


if __name__ == '__main__':
    print(main())
    print('main - done')