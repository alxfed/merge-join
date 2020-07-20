# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
from datetime import datetime
from numpy.random import randn


def multicolumn(row):
    month = row['index'].month
    day = row['index'].day
    hour = row['index'].hour
    # https://docs.python.org/3/tutorial/inputoutput.html?highlight=numbers%20output%20formatting
    mm = f'{month:02d}'
    dd = f'{day:02d}'
    hh = f'{hour:02d}'
    return pd.Series([mm, dd, hh, month, day, hour])


def main():
    dti = pd.date_range(start='2020-04-21 20:00:00', end=datetime.now(), freq='H')
    data = pd.DataFrame(randn(len(dti), 2), columns=['rand1', 'rand2'], index=dti)
    data.reset_index(drop=False, inplace=True)
    data[['mm', 'dd', 'hh', 'month', 'day', 'hour']] = data.apply(multicolumn, axis='columns')
    data.drop(columns=['rand1', 'rand2'], inplace=True)
    return


if __name__ == '__main__':
    main()
    print('main - done')