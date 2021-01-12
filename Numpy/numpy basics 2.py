# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:32:01 2021

@author: Shrey
"""

import numpy as np
a=np.array([[2,3,4],[5,7,1],[6,2,5]])
b=np.array([[4,3,5],[2,6,7],[1,5,6]])
c=a+b #for addition of two matrix
d=a.dot(b) #for multiplication of two matrix
print(c)
print(d)
#for acess Row
print(a[0])
print(a[-1])
#for access column
print(a[:,0])
print(a[:,2])
print(a[:2,:2])
print(a[:,-1])
ar=np.matrix(np.arange(12).reshape((4,3)))
print(ar)
y1=ar[0]
print(y1)
print(ar==y1)
print((ar==y1).all(0))
print((ar==y1).all(1))

d=np.array([[1,2,3],[4,5,6]])
e=np.array([[7,8,9],[10,11,12]])
print(np.vstack((d,e)))
print(np.hstack((d,e)))

