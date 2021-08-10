# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 22:37:06 2021
@title: 06 輸入與輸出教學
@author: shannon
"""
# 註解/ 複製Ctrl+C 剪下Ctrl+X 貼上Ctrl+V / 全選Ctrl+A 
# 上一步 Ctrl+Z 下一步 Ctrl+Y
# a = 1
# print(a) # Ctrl + 1
# a += 1
# print(a) 
# Ctrl + 1(解開+註解), Ctrl+4(區域), Ctrl+5(解開註解), Ctrl+/ (spyder無法用)
# Win + 句號 (言文字)

# 輸入函式input (ctrl+1單行註解) (Ctrl+4區域 Ctrl+5取消區域註解)
# =============================================================================
# account = input("請輸入您的帳號=>")
# print(account,"這是你嗎?")
# =============================================================================

# 輸出函式print (ctrl+R替換)
print("me print")
print("me", "print", "!","@")
print("me","print","hello", sep="_", end="!")

# 輸出函式  格式化format
a = 2
b = 3
print(f"{a} * {b} = {a*b}")

# 如果想要格式化設定 format
# 1. 後面加冒號: 
# 2. +號表示要顯示正負號
# 3. 5.1表示長度至少5個字元, 小數保留1位, float表示以符點數輸出常用的還有d(整數)s(字串)
pi = 3.1415926
a = 6.0
print(f"圓周率是{pi},乘上{a}是{pi*a:+15.2f}")




