# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd

if __name__ == '__main__':
    json = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
            {'name': {'given': 'Mose', 'family': 'Regner'}},
            {'id': 2, 'name': 'Faye Raker'}]
    norm = pd.json_normalize(data=json)
    print('\ndone')