# -*- coding: utf-8 -*-
"""examples of .where and .mask
"""
import pandas as pd


def condition(frame):
    a = frame  # Yes, this is the whole frame here.
    return frame


def oth(frame):
    b = frame
    return frame


def main():
    data = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 3],
         [7, 8, 3]], index=[1, 2, 3], columns=['a', 'b', 'c']
    )
    df = data.copy()
    df2 = data.copy()
    # condition = (data == 3)
    replacement = df.mask(cond=condition, other=oth)
    other_replacement = df2.where(cond=condition, other=oth)
    print(other_replacement)
    return

if __name__ == '__main__':
    main()
    print('\ndone')