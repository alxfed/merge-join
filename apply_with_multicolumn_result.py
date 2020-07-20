# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
from datetime import datetime
from numpy.random import randn


def multicolumn(row):
    a = row['index'].month
    b = row['index'].day
    c = row['index'].hour
    return pd.Series([a, b, c])


def main():
    dti = pd.date_range(start='2020-04-21 20:00:00', end=datetime.now(), freq='H')
    # sse = dti.to_series(name='daytime')
    # dt = list(dti)
    data = pd.DataFrame(randn(len(dti), 2), columns=['rand1', 'rand2'], index=dti)
    data.reset_index(drop=False, inplace=True)
    # se = data.index.to_series()
    data[['mm', 'dd', 'hh']] = data.apply(multicolumn, axis='columns')
    data.drop(columns=['rand1', 'rand2'], inplace=True)
    return


if __name__ == '__main__':
    main()
    print('main - done')