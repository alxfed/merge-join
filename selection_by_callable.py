# -*- coding: utf-8 -*-
"""
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html?#selection-by-callable
"""
import pandas as pd
import numpy as np


def main():
    data = pd.DataFrame(np.random.randn(6, 4),
                        index = list('abcdef'),
                        columns = list('ABCD'))
    indexed = data.loc[lambda df: df.A > 0, :]
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')