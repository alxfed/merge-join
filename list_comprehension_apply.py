# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np
from timeit import timeit


def main():
    d = """data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=[0, 1, 2], columns= ['col_1', 'col_2', 'col_3']
    )
    """

    s = """mult = [c1*c3 for c1,c3 in zip(data['col_1'], data['col_3'])]"""
    a = timeit(stmt=s, setup=d)
    b = True
    return a


if __name__ == '__main__':
    a = main()
    print('main - done', a)

''' Unzip with the help of * operator
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True
'''