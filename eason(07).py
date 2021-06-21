# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:38:55 2021

@author: USER
"""

a=int(input("請輸入月租費形式:"))
b=int(input("請輸入通話時間:"))

if a==186 and b<=2067:
    print("通話費為"+str(a))
elif a==186 and b>2067:
    i=b/2067
    if i>2:
        x=b*0.09
        y=x*0.8
        print("通話費為"+str(y))
    else:
        x=b*0.09
        y=x*0.9
        print("通話費為"+str(y))
elif a==386 and b<=4825:
    print("通話費為"+str(a))
elif a==386 and b>4825:
    i=b/4825
    if i>2:
        x=b*0.08
        y=x*0.7
        print("通話費為"+str(y))
    else:
        x=b*0.08
        y=x*0.8
        print("通話費為"+str(y))
if a==586 and b<=8371:
    print("通話費為"+str(a))
elif a==586 and b>8371:
    i=b/8371
    if i>2:
        x=b*0.07
        y=x*0.6
        print("通話費為"+str(y))
    else:
        x=b*0.07
        y=x*0.7
        print("通話費為"+str(y))
if a==986 and b<=16433:
    print("通話費為"+str(a))
elif a==586 and b>16433:
    i=b/16433
    if i>2:
        x=b*0.06
        y=x*0.5
        print("通話費為"+str(y))
    else:
        x=b*0.06
        y=x*0.6
        print("通話費為"+str(y))
    

        
    
        