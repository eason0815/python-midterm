# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:54:00 2021

@author: USER
"""

xx=input("22:")
a=xx.split(" ")[0]
b=xx.split(" ")[1]
c=xx.split(" ")[2]
d=xx.split(" ")[3]
e=xx.split(" ")[4]
if a=="A":
    a=1
elif a=="J":
    a=11
elif a=="Q":
    a=12
elif a=="K":
    a=13    
else:
    a=int(a)
if b=="A":
    b=1
elif b=="J":
    b=11
elif b=="Q":
    b=12
elif b=="K":
    b=13    
else:
    a=int(a)
if c=="A":
    c=1
elif c=="J":
    c=11
elif c=="Q":
    c=12
elif c=="K":
    c=13    
else:
    a=int(a)
if d=="A":
    d=1
elif d=="J":
    d=11
elif d=="Q":
    d=12
elif d=="K":
    d=13    
else:
    a=int(a)
if e=="A":
    e=1
elif e=="J":
    e=11
elif e=="Q":
    e=12
elif e=="K":
    e=13    
else:
    a=int(a)
total=sum(a,b,c,d,e)
print(total)

