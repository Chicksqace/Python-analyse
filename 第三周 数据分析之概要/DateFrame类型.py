#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/27 18:41
# @File : DateFrame类型.py
import pandas as pd
import numpy as np
# d=pd.DataFrame(np.arange(10).reshape(2,5))
# print(d)
# dt={'one':pd.Series([1,2,3],index=['a','b','c']),
# 'two':pd.Series([11,22,33],index=['a','bc','c']),
#     }
# d=pd.DataFrame(dt)
# print(d)
dt={'one':[1,23,3],'two':[12,23,33]}
d=pd.DataFrame(dt,index=['a','b','d'])
print(d)