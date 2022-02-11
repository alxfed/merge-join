# -*- coding: utf-8 -*-
"""...
"""
from pydantic import BaseModel


class this(BaseModel):
    a: str
    b: str

the = {"a": "one", "b": 'two', "c": 3}

what = this(**the)

print('ok')  # !!!