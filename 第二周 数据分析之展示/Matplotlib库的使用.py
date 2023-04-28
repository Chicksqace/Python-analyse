#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 18:18
# @File : Matplotlib库的使用.py
import matplotlib.pyplot as plt
# 出图片
# plt.plot([2,1,6,4,5])
# plt.ylabel("grade")
# plt.show()
# 保存
# plt.plot([2,1,6,4,5])
# plt.ylabel("grade")
# plt.savefig('test',dpi=600)
# plt.show()
#plt.plot(x,y)当有两个以上参数时，按照X轴和Y轴顺序绘制数据点
# plt.plot([1,2,3,4,5],[2,1,6,4,5])
# plt.ylabel("grade")
# plt.axis([-1,10,0,6])
# plt.show()

# 绘图区域
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return  np.exp(-t)*np.cos(2*np.pi*t)
a=np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()