# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    data= pd.DataFrame(
        [[1, 7, 3, 1],
         [2, 5, 6, 2],
         [3, 8, 0, 3]], index=[0, 1, 2], columns= ['a', 'b', 'c', 'd']
    )
    ord = data['d']
    data.drop(columns='d', inplace=True)
    cor = data.corrwith(other=ord, axis='index', method='pearson')
    print('ok', cor)


if __name__ == '__main__':
    main()
    print('\ndone')