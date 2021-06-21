# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:56:53 2021

@author: USER
"""
a=list(input("輸入月及日:").split(' '))
if 2>int(a[0])>0:
    if int(a[1])<18:
        print("Capricorn")
    elif int(a[1])>18:
        print("Aquarius")
if 3>int(a[0])>1:
    if int(a[1])<20:
        print("Aquarius")
    elif int(a[1])>20:
        print("Pisces")
if 4>int(a[0])>2:
    if int(a[1])<20:
        print("Pisces")
    elif int(a[1])>20:
        print("")
if 5>int(a[0])>3:
    if int(a[1])<21:
        print("Aries")
    elif int(a[1])>21:
        print(" Taurus")
if 6>int(a[0])>4:
    if int(a[1])<21:
        print("Taurus")
    elif int(a[1])>21:
        print("Gemini")
if 7>int(a[0])>5:
    if int(a[1])<22:
        print("Gemini")
    elif int(a[1])>22:
        print(" Cancer")
if 8>int(a[0])>6:
    if int(a[1])<18:
        print("Cancer")
    elif int(a[1])>18:
        print("Leo")
if 9>int(a[0])>7:
    if int(a[1])<18:
        print("Leo")
    elif int(a[1])>18:
        print(" ")
if 10>int(a[0])>8:
    if int(a[1])<18:
        print("Virgo")
    elif int(a[1])>18:
        print(" Libra")
if 11>int(a[0])>9:
    if int(a[1])<18:
        print("Libra")
    elif int(a[1])>18:
        print("Scorpio")
if 12>int(a[0])>10:
    if int(a[1])<18:
        print("Scorpio")
    elif int(a[1])>18:
        print(" Sagittarius")
if 13>int(a[0])>11:
    if int(a[1])<18:
        print("Sagittarius")
    elif int(a[1])>18:
        print("Capricorn")