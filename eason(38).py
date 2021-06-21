# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:47:04 2021

@author: USER
"""

n=int(input("輸入n:"))

for i in range(1,(n+1)//2+1):
    print(" "*(n-i)+"*"*(2*(i-1)+1))
for j in reversed(range(1,(n+1)//2)):
    print(" "*(n-j)+"*"*(2*(j-1)+1))