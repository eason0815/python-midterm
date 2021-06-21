# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:33:19 2021

@author: USER
"""

a=int(input("組數 :"))
b,c=map(int,input("第一組 :").split())
d,e=map(int,input("第二組 :").split())
f,g=map(int,input("第三組 :").split())

totala=(b*250)+(c*175)
totalb=(d*250)+(e*175)
totalc=(f*250)+(g*175)


print("第一組應收費用 :"+str(totala))
print("第二組應收費用 :"+str(totalb))
print("第三組應收費用 :"+str(totalc))

    
