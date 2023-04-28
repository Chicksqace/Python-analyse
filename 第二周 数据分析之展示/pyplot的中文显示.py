#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 20:46
# @File : pyplot的中文显示.py
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.family']='STSong'
# matplotlib.rcParams['font.size']=20
#
# a=np.arange(0.0,5.0,0.02)
#
# plt.xlabel('x轴：时间')
# plt.ylabel('y轴：振幅')
# plt.plot(a,np.cos(2*np.pi*a),'r--')
# plt.show()

# 第二种方法

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

a=np.arange(0.0,5.0,0.02)

plt.xlabel('x轴：时间',fontproperties='SimHei',fontsize=20)
plt.ylabel('y轴：振幅',fontproperties='SimHei',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()