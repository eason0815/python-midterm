# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:54:33 2021

@author: USER
"""

a=input("請輸入A的好友:").split(' ')
b=input("請輸入B的好友:").split(' ')
c=[]

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print(c)

