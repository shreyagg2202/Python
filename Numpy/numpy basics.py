# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:59:12 2021

@author: Shrey
"""

import numpy as np
z = np.zeros([2,5])
print(z)
r=np.arange(15)
print(r)
s=np.linspace(2,5,5)
print(s)
t=np.identity(15)
print(t)
u=np.array([[1,2,3,4],[11,22,233,44]])
print(u)
t=u.T
print(t)
b=np.array([[1,2,3],[11,22,33],[7,8,9]])
print(b)
b.sum(axis=0)
b.sum(axis=1)
for i in b.flat:
    print(i)
    
    
q=[10,20,30]
e=[4,56,6]
s=np.add(q,e)
f=np.append(q,e)
print(f)
m=np.multiply(q,e)
print(m)
d=np.divide(q,e)
print(d)
sub=np.subtract(q,e)
print(sub)