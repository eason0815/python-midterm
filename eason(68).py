# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:49:21 2021

@author: USER
"""

a=list(input("請輸入第一組數字 :"))
b=list(input("請輸入第二組數字 :"))

i=0
j=0
eason=0
nose=0
nothing=0
while i<4:
    if a[i]==b[i]:
        eason=eason+1
    elif j<4:
        for j in range(len(b)):
            if a[i]==b[j]:
                if i==j:
                    break
                else:
                    nose=nose+1
            else:
                nothing=nothing-1
    i=i+1

if nothing < eason or nothing < nose and nothing==0:
    print(str(eason)+"A"+str(nose)+"B")
if nothing==-4:
    print("0A"+"0B")



  
        
    


        
    
    
       


    
        
    
    