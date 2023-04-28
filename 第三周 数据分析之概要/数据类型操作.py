#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/27 19:03
# @File : 数据类型操作.py
import pandas as pd
dl={'城市':['北京','上海','广西','广东'],
    '值1':[111,233,456,32],
    '值2':[1311,2233,1456,332],
    '值3':[211,533,956,322]
    }
d=pd.DataFrame(dl,index=['c1','c2','c3','c4'])
# print(d)
d=d.reindex(index=['c4','c3','c2','c1'])
# print(d)
# d=d.reindex(columns=['值3','值2','值1','城市'])
# print(d)
# newc=d.columns.insert(4,'新增')
# newd=d.reindex(columns=newc,fill_value=200)
# print(newd)
print(d.index)
print(d.columns)