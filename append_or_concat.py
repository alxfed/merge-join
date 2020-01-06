# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data1 = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'b', 'c'], columns= [10, 11, 12]
    )
    data2 = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]], index=['a', 'e', 'c'], columns= [1, 11, 2]
    )
    result = pd.concat(objs=[data1, data2], axis=1)
    # ignore_index just drops the index from the result and replaces it with {RangeIndex: 6}
    return


if __name__ == '__main__':
    main()
    print('main - done')