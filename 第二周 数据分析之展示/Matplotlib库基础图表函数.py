#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/26 13:46
# @File : Matplotlib库基础图表函数.py
# pyplot饼图的绘制
import matplotlib.pyplot as plt
import numpy as np
# labels='Frogs','Hogs','Dogs','Logs'
# sizes=[15,30,45,10]
# explode=(0,0.1,0,0)
# plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
# plt.show()

# labels='Frogs','Hogs','Dogs','Logs'
# sizes=[15,30,45,10]
# explode=(0,0.1,0,0)
# plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
# plt.axis('equal')
# plt.show()
# pyplot直方图的绘制
# np.random.seed(0)
# 随机种子为0
# mu,sigma=100,20
# a=np.random.normal(mu,sigma,size=100)#均值和方差正态分布
# plt.hist(a,20,histtype='stepfilled',facecolor='b',alpha=0.75)
# plt.title('Histogram')
# plt.show()
# mu,sigma=100,20
# a=np.random.normal(mu,sigma,size=100)#均值和方差正态分布
# plt.hist(a,40,histtype='bar',facecolor='r',edgecolor='g',alpha=0.75)
# plt.title('Histogram')
# plt.show()
# pyplot极坐标的绘制
# import matplotlib.pyplot as plt
# import numpy as np
# n=20
# theta=np.linspace(0.0,2*np.pi,n,endpoint=False)
# redii=10*np.random.rand(n)
# width=np.pi/4*np.random.rand(n)
# ax=plt.subplot(111,projection='polar')
# bars=ax.bar(theta,redii,width=width,bottom=0.0)
# for r,bar in zip(redii,bars):
#     bar.set_facecolor(plt.cm.viridis(r/10.))
#     bar.set_alpha(0.5)
# plt.show()

# pyplot散点图的绘制
fig,ax=plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')
plt.show()