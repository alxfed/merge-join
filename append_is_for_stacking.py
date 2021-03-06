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
    result = data1.append(data2, sort=None)
    result2 = data1.append(data2, ignore_index=True)
    # ignore_index just drops the index from the result and replaces it with {RangeIndex: 6}
    return


if __name__ == '__main__':
    main()
    print('main - done')