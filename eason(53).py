# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:54:45 2021

@author: USER
"""
xx=float(input("請輸入里程公里數(km) :"))
km=xx*1000
money=(km-1500)/250
if money > 1:
    cash=75+money*5
    print("所需車資為 :"+str(cash))
else:
    cash2=75+5
    print("所需車資為 :"+str(cash2))