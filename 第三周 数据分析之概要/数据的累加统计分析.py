#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/4 19:07
# @File : 数据的累加统计分析.py
import pandas as pd
import numpy as np
# b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
# print(b)
# print(b.cumsum())
# print(b.cummin())
# print(b.cummax())

b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)
print(b.rolling(2).sum())
print(b.rolling(3).sum())