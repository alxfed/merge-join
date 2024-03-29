# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def pmi(first, second, **kwargs):
    p = kwargs['a']
    scalar = 0.0 # float
    print('ok')
    return scalar


def main():
    p = {'a': 0}
    data = pd.DataFrame(
        {'a': [1, 2, 3],
         'b': [4, 5, 6],
         'c': [7, 8, 9]}
    )
    co = data.corr(method=pmi, **p)
    obj = co.style.background_gradient(cmap='coolwarm').set_precision(2)
    obj.to_excel("output.xlsx")
    return


if __name__ == '__main__':
    main()
    print('\ndone')
