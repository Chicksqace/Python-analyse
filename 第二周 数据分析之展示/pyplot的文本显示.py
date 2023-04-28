#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 21:39
# @File : pyplot的文本显示.py
import numpy as np
import matplotlib.pyplot as plt
a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel('时间',fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel('振幅',fontproperties='SimHei',fontsize=15)
plt.title(r'正弦波实例$y=cos(2\pi x)$',fontproperties='SimHei',fontsize=20)
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.text(2,1,r'$\mu=100$',fontsize=15)
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()