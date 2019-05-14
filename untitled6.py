# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:36:48 2019

@author: User
"""

income = int(input("請輸入今年收入淨額："))
print("付稅金額：",end="")
if(income >= 2000000):
    print(income*0.3, end=" 元\n")  
elif(income >= 1000000):
    print(income*0.21, end=" 元\n")
elif(income >= 600000):
    print(income * 0.13, end=" 元\n") 
elif(income >= 300000):
    print(income * 0.06, end=" 元\n") 
else:
    print(income *0, end=" 元\n")