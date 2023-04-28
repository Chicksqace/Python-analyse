#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/7 23:20
# @Author : 不知天文，不知地理
# @File : Numpy数据存取与函数.py
import numpy as np
# a=np.arange(100).reshape(5,20)
# print(a)
# np.savetxt('a.csv',a,fmt='%d',delimiter=',')
# np.savetxt('a.csv',a,fmt='%f',delimiter='-')

# b=np.loadtxt('a.csv',dtype=np.int32,delimiter='-')
# print(b)

# a=np.arange(100).reshape(5,10,2)
# b=a.tofile("b.dat",format="%d")
# print(b)
#
# a=np.arange(100).reshape(5,10,2)
# a.tofile("b.dat",sep=",",format="%d")
# c=np.fromfile("b.dat",dtype=np.int32,sep=",").reshape(5,10,2)
# print(c)

# a=np.arange(100).reshape(5,10,2)
# np.save("a.npy",a)
# b=np.load("a.npy")
# print(b)

# a=np.random.randint(100,200,(3,5))
# print(a)
# np.random.seed(10)
# b=np.random.randint(100,200,(3,5))
# print(a)
# np.random.seed(10)
# a=np.random.randint(100,200,(3,5))

# a=np.random.randint(100,200,(3,4))
# print(a)
# np.random.shuffle(a)
# print(a)

# b=np.random.randint(100,200,(8,))
# print(b)
# print(np.random.choice(b,(3,2)))
# print(np.random.choice(b,(3,2),replace=False,p=b/np.sum(b)))

a=np.arange(15).reshape(3,5)
print(a)
print(np.sum(a))
print(np.mean(a,axis=1))
print(np.mean(a,axis=0))
print(np.average(a,axis=0,weights=[10,5,1]))
print(np.std(a))
print(np.var(a))