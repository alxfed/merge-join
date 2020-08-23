# -*- coding: utf-8 -*-
"""...
"""
# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data = pd.DataFrame(
        [['a', '\\"2', 'b'],
         [4, 5, 6],
         [7, 8, 0]], columns=[10, 11, 12]
    )
    data[11] = data[11].replace(r'\\', '', regex=True)
    return


if __name__ == '__main__':
    main()