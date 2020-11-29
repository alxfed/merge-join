# -*- coding: utf-8 -*-
"""https://www.freecodecamp.org/news/dynamic-class-definition-in-python-3e6f7d20a381/

With three arguments, return a new type object.
This is essentially a dynamic form of the class statement.
The name string is the class name and becomes the __name__ attribute;
the bases tuple itemizes the base classes and becomes the __bases__ attribute;
and the dict dictionary is the namespace containing definitions for class
body and is copied to a standard dictionary to become the __dict__ attribute.
For example, the following two statements create identical type objects:

class X:
    a = 1


X = type('X', (object,), dict(a=1))

"""
from dataclasses import dataclass


X = type('X', (object,), dict(a=1))

"""
https://realpython.com/python-data-classes/

https://docs.python.org/3/library/dataclasses.html?highlight=dataclasses#module-dataclasses

dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)

Creates a new dataclass with name cls_name, fields as defined in fields, 
base classes as given in bases, and initialized with a namespace as given in namespace. 
fields is an iterable whose elements are each either name, (name, type), or (name, type, Field). 
If just name is supplied, typing.Any is used for type. The values of init, repr, eq, order, 
unsafe_hash, and frozen have the same meaning as they do in dataclass().

This function is not strictly required, because any Python mechanism for creating a new class 
with __annotations__ can then apply the dataclass() function to convert that class to a dataclass. 
This function is provided as a convenience. For example:
"""



