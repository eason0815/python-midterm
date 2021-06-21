# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:00:07 2021

@author: USER
"""

a=int(input("x:"))
b=int(input("y:"))

if a>0 and b>0:
    i=a**2+b**2
    print("該點位於第一象限，"+"離原點距離為根號"+str(i))
elif a>0 and b<0:
    i=a**2+b**2
    print("該點位於第二象限，"+"離原點距離為根號"+str(i))
elif a<0 and b<0:
    i=a**2+b**2
    print("該點位於第三象限，"+"離原點距離為根號"+str(i))
elif a<0 and b>0:
    i=a**2+b**2
    print("該點位於第四象限，"+"離原點距離為根號"+str(i))
elif a==0 and b==0:
    print("該點位於原點:")
elif a==0 and b>0:
    i=a**2+b**2
    print("該點位於上半平面Y軸上，"+"離原點距離為根號"+str(i))
elif a==0 and b<0:
    i=a**2+b**2
    print("該點位於下半平面Y軸上，"+"離原點距離為根號"+str(i))
elif a>0 and b==0:
    i=a**2+b**2
    print("該點位於右半平面X軸上，"+"離原點距離為根號"+str(i))
elif a<0 and b==0:
    i=a**2+b**2
    print("該點位於左半平面X軸上，"+"離原點距離為根號"+str(i))


    