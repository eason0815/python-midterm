# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:59:24 2021

@author: USER
"""

a=('紅豆生南國，春來發幾枝?願君多採擷，此物最相思。')
b=('春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。')
newa={x.replace('，', '').replace('。', '').replace('?', '') for x in a}
newb={y.replace('，', '').replace('。', '').replace('?', '') for y in b}
print(set(newa)&set(newb))