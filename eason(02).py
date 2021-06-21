# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=int(input("請輸入度數:"))

if a<=120:
    i=a*2.1
    j=a*2.1
    print("Summer months:%4.2f"%(i))
    print("Non-Summer months:%4.2f"%(j))
elif 121<a<330:
    i=a*3.02
    j=a*2.68
    print("Summer months:%4.2f"%(i))
    print("Non-Summer months:%4.2f"%(j))
elif 331<a<500:
    i=a*4.39
    j=a*3.61
    print("Summer months:%4.2f"%(i))
    print("Non-Summer months:%4.2f"%(j))
elif 501<a<700:
    i=a*4.97
    j=a*4.01
    print("Summer months:%4.2f"%(i))
    print("Non-Summer months:%4.2f"%(j))
elif a>701:
    i=a*5.63
    j=a*4.5
    print("Summer months:%4.2f"%(i))
    print("Non-Summer months:%4.2f"%(j))