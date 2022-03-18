# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import datetime as dt
import numpy as np


def main():
    time_delta_data = pd.DataFrame(
        [[dt.datetime(2022, 3, 11), dt.datetime(2022, 3, 11), 0],
         [dt.datetime(2022, 3, 11),dt.datetime(2022, 3, 12), 6],
         [dt.datetime(2022, 3, 11), dt.datetime(2022, 3, 13), 0]], index=[0, 1, 2], columns= ['install', 'first_pay', 'time_delta']
    )

    data = [pd.Timedelta('0 days'), pd.Timedelta('1 days'), pd.Timedelta('2 days')]
    td_index = pd.TimedeltaIndex(data=data, unit='D', name='td_index')
    td_df = pd.DataFrame(index=td_index)
    result = time_delta_data.reindex(index=td_index)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')