# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:18:21 2021

@author: USER
"""

a=int(input("請輸入遊戲時間:"))
b=a*60
c=b/30
d=c/3
if d >=1:
    i=d*35
    j=c%3
    if j==1:
        x=1*11
        print(str(i+x)+"支兵")
    elif j==2:
        y=2*23
        print(str(i+y)+"支兵")
    elif j==0:
        print(str(i)+"支兵")

