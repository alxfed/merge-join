# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c'], columns= [10, 11, 12]
    )
    data2 = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c'], columns= [10, 11, 12]
    )

    return


if __name__ == '__main__':
    main()
    print('main - done')