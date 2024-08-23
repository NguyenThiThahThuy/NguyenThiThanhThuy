# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:51:52 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
N = int(input("Nhập số có 2 chữ số: "))
if 10 <= N <= 99:
    hangchuc = N // 10
    hangdonvi = N % 10
    tong = hangchuc + hangdonvi
    print("Tổng các chữ số của {N} là: {hangchuc} + {hangdonvi} = {tong}")
else:
    print("không hợp le !")

    
    
    
