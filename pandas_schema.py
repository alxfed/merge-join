# -*- coding: utf-8 -*-
""" Pandas native schema
"""
import pandas as pd


df = pd.DataFrame(
    {
        "foo": [1, 2, 3, 4],
        "bar": ["a", "b", "c", "d"],
        "baz": pd.date_range("2018-01-01", freq="d", periods=4),
        "qux": pd.Categorical(["a", "b", "c", "c"]),
    },
    index=pd.Index(range(4), name="idx"),
)

df.to_json("test.json", orient="table")

new_df = pd.read_json("test.json", orient="table")

print('ok')