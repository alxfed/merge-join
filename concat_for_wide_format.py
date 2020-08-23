# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], columns=[10, 11, 12]
    )
    addition = pd.Series([1, 2, 3, 4], name=13)
    new_data = pd.concat(objs=[data, addition], axis=1)
    return


if __name__ == '__main__':
    main()
    print('\ndone')