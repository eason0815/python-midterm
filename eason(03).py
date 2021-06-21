# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:41:18 2021

@author: USER
"""
a=int(input("請輸入西元年:"))
b=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]

if a%12==4:
    print(b[1])
elif a%12==5:
    print(b[2])
elif a%12==6:
    print(b[3])
elif a%12==7:
    print(b[4])
elif a%12==8:
    print(b[5])
elif a%12==9:
    print(b[6])
elif a%12==10:
    print(b[7])
elif a%12==11:
    print(b[8])
elif a%12==12:
    print(b[9])
elif a%12==1:
    print(b[10])
elif a%12==2:
    print(b[11])
elif a%12==3:
    print(b[12])