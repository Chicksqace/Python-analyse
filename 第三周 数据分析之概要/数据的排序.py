#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/3 19:35
# @File : 数据的排序.py
import pandas as pd
import numpy as np
b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','b','d'])
# print(b)
# print(b.sort_index())
# print(b.sort_index(ascending=False))
# print(b)
# print(b.sort_index(axis=1,ascending=False))
# print(b.sort_index())
print(b)
print(b.sort_values(2,ascending=False))
print(b.sort_values('a',axis=1,ascending=False))
