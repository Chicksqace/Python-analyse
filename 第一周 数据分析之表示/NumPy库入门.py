#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/1 20:08
# @Author : 不知天文，不知地理
# @File : NumPy库入门.py
import numpy as np
# a=np.array([[0,1,2,3,4,5],[2,3,4,5,6,8]])
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(a.itemsize)

# ndarray数组的创建
# 1.列表创建
# x=np.array([0,1,2,3])
# print(x)
# # 2.函数创建ndarray数组
# a=np.arange(10)
# print(a)
# b=np.ones((3,6))
# print(b)
# c=np.zeros((3,6),dtype=np.int32)
# print(c)
# d=np.eye(5)
# print(d)
# e=np.full((2,2),'2')
# print(e)
# print(e.shape)
# a=np.linspace(1,-2,4)
# d=np.linspace(1,2,4)
# print(a)
# print(d)
# b=np.linspace(1,2,4,endpoint=False)
# print(b)
# c=np.concatenate((a,b))
# print(c)

# 数组的维度变化
a=np.ones((2,3,4),dtype=np.int32)
# 原数组不变
# a.reshape((3,8))
# print(a)
# print('------------')
# b=np.ones((2,3,4),dtype=np.int32)
# # 原数组变
# b.reshape((3,8))
# print(b)
# print('------------')
# a=np.ones((2,3,4),dtype=np.int32)
# c=a.flatten()
# # 不修改原值
# print(c)
# print('------------')

# ndarray数组的类型变换

# a=np.ones((2,3,4),dtype=np.int32)
# print(a)
# b=a.astype(np.float32)
# print(b)

# a=np.full((2,3,4),25,dtype=np.int32)
# print(a)
# b=a.tolist()
# print(b)

# 多维数组的切片：
# a=np.arange(24).reshape((2,3,4))
# print(a)
# print('------------')
# print(a[:,1,-3])
# print('------------')
# print(a[:,:,::2])
# a=np.arange(24).reshape((2,3,4))
# print(a)
# print('------------')
# a=a/a.mean()
# print(a)

a=np.arange(24).reshape((2,3,4))
b=np.square(a)
print(a)
print('------------')
print(b)
c=np.sqrt(a)
print('------------')
print(c)

# a=np.arange(24).reshape((2,3,4))
# b=np.square(a)
# print(np.maximum(a,b))
