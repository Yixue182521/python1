# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:18:41 2019

@author: User
"""
money = int(input("請輸入購物金額:"))
if(money >= 10000):
    if(money>=100000):
        print(money*0.8, end="元/n")
    elif(money >= 50000):
        print(money*0.85, end="元/n")
    elif(money >= 30000):
        print(money*0.9, end="元/n")
    elif(money >= 10000):
        print(money*0.95, end="元/n")
    else:
        print(money, end="元/n")