#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/27 17:23
# @File : Series类型.py
import pandas as pd
import numpy as np
# b=pd.Series([9,8,7,6],index=['a','s','c','f'])
# 其他函数创建
# b=pd.Series(range(5),index=range(5))
# m=pd.Series(np.arange(5),index=np.arange(9,4,-1))
# print(b)
# print(m)
# print(m.index)
# print(m.values)
# 切片
# b=pd.Series([9,6,5,3],['a','b','c','d'])
# print(b)
# print(b[3])
# print(b['a'])
# print(b[:3])
# print(b[b>b.median()])
# np.exp(b)

b=pd.Series([9,6,5,3],['a','b','c','d'])
b['a','b']=20
print(b)
# print(b['b'])
# print('c' in b)
# print(0 in b)
# print(b.get('f',100))