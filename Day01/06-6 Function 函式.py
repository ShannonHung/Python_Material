# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:30:32 2021
@title: 2-1 Function
@author: shannon
"""
# function的基本寫法: 
# =============================================================================
# def hello():
#     print("你好我是function")
# hello()
# =============================================================================

# function帶有參數
# =============================================================================
# def circle(r):
#     return r*r*3.14
# 
# # function 參數給予原本的初始值
# def circle2(r=1):
#     return r*r*3.14
# 
# # funciton: 長方形面積
# def area(w, h, d):
#     return w*h*d
# 
# # function: 非數字也可以喔~
# def welcome(name, title="先生/小姐", content="你好"):
#     print(name + title + content)
# =============================================================================

# 不定數目的參數: *args容器 (argument)
# =============================================================================
# def printSum(content, *args): # args使用tuple裝起來了
#     print(content, args, '=', sum(args))
# # printSum("加總", 1,2,3)
# =============================================================================

# 不定數目的參數: **kwargs字典 (keyword) 有兩個星星
# =============================================================================
# def printPrice(content, **kwargs): # kwargs被打包成dict
#     print(content, kwargs) # kwargs可以改名
# printPrice("購物車", 包包=50, 水壺=30) # 注意不用加上"string"
# =============================================================================

# args容器 + kwargs字典 合併
# =============================================================================
# def combine(content, *container, **dictionary):
#     print(content, container, ':', dictionary, sep=' ')
# 
# list1 = ['test1','test2'] # 就換使用list最終也會轉成tuple
# dict1 = {'1':1, '2':2}
# combine("test",*list1, **dict1)
# =============================================================================

# 變數的有效範圍 Scope Rule
# =============================================================================
# a = b = c = 1 # 建立a,b,c 三個全域變數
# def test(b): # 參數b為區域變數
#     # global a # 可以使用global指名要使用全域變數
#     a = 2 # 建立區域變數a
#     print(a,b,c) # 輸出區域變數a,b及全域變數c
# test(3)
# print(a,b,c) # a,b為區域變數; c為全域變數
# =============================================================================

# 容器物件的scope role
# =============================================================================
# s = [1,2,3]
# t = [4,5,6]
# 
# def test(a): # 不是區域變數 參數a會綁訂到傳入的串列
#     a[0] = 'aaa' # 改寫區域變數a的內容
#     t[0] = 'bbb' # 改寫全域容器內容
#     s = [7,8,9] # 建立一個新的區域變數s
#     s[0] = '777' # 只會影響區域變數的s 不影響全域變數的s
#     print("In Funciton =>",s,t) # 輸出s,t看看
# test(s)
# print("Outside =>", s,t)
# 
# =============================================================================


# Q3: (改之前) 可以讓老師先輸入班級人數(假設10人)，然後使用For迴圈讓老師輸入所有人的成績，輸入完之後可以告訴老師班級總分及平均(取小數點第二位)
# =============================================================================
# number = int(input("請輸入班級人數:"))
# scores = []
# total = 0
# count = 0;
# while (count < number):
#     try:
#         score = int(input("請輸入成績:"))
#         if(score >= 0 and score <= 100):
#             count +=1
#             total += score
#             scores.append(score)
#         else:
#             print("成績異常請重新輸入")
#             continue
#     except:
#         print("成績異常請重新輸入")
#         continue
# 
# print("全班共有", number, '人')
# print("總分是: ", total)
# print(f"平均是: {total/len(scores):5.2f}")    
# =============================================================================

# Q3: 改之後
# =============================================================================
# number = int(input("請輸入班級人數:"))
# scores = []
# total = 0
# count = 0;
# while (count < number):
#     try:
#         score = int(input("請輸入成績:"))
#         if(score >= 0 and score <= 100):
#             count +=1
#             scores.append(score)
#         else:
#             print("成績異常請重新輸入")
#             continue
#     except:
#         print("成績異常請重新輸入")
#         continue
# 
# def average(scores):
#     for i in scores:
#         global total
#         total += i
#     print(total)
#     return total/ len(scores)
# 
# 
# print("全班共有", number, '人')
# print("總分是: ", total)
# print(f"平均是: {average(scores):5.2f}")    
# =============================================================================
