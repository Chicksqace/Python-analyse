#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/4 20:51
# @File :  实例：房价增幅与M2增幅的相关性.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('mac72-uber3.csv', index_col=0)
price_increase = df['House price growth']
m2_increase = df['M2 increase']
corr = np.corrcoef(price_increase, m2_increase)[0, 1]
print('相关系数:', corr)

plt.plot(price_increase, label='House price growth')
plt.plot(m2_increase, label='M2 increase')
plt.legend()
plt.show()