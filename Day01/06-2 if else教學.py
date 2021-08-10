# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 23:08:35 2021
@title: 06-2 if教學
@author: shannon
"""

# If 基礎


## if超級簡寫 1行搞定 也有一樣的效果喔
# =============================================================================
# a = 1 # a 叫做0
# 
# if (a==0): # 如果是True就會做空四格的程式碼
#     print("你真聰明答對了!") # 一定要空四格!!!! 或是一個tab
#     a = a + 1  # 如果是(a==0)是True我就把a加一
# print("我一定被印出來", a)      
# =============================================================================

# If...elif...else...基礎 (BMI示範)
## If(判斷式), elif(判斷式), else不用判斷式
# =============================================================================
# bmi = 0
# if (0 < bmi < 18.5): # False
#     print("體重過輕")
# elif (bmi >= 18.5 and bmi < 24): # else if (判斷) : True and False = False
#     print("你很健康") 
# elif (bmi >= 24 and bmi < 27): # True and False = False
#     print("過重")
# elif (bmi >= 27 and bmi < 30): # True and True = True
#     print("輕度肥胖")
# elif (bmi >= 30 and bmi <= 35):
#     print("中度肥胖")
# elif (bmi >= 35):
#     print("重度肥胖")
# else:
#     print("你的數字可能有問題?")
# =============================================================================


# 課堂練習 input + if + elif + else 的BMI應用
## float => str 轉乘 float 有小數點, input 可以讓使用者輸入資料
# =============================================================================
# weight = float(input("請輸入你的體重(kg)"))
# height = float(input("請輸入你的身高(cm)"))
# print(f"{height}是身高, {weight}是體重")
# ## 算使用者的bmi: 體重/身高(m)平方
# bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
# print(f"BMI是{bmi:+5.2f}")
# ## 目前bmi狀態
# if (0 < bmi < 18.5): # False
#     print("體重過輕")
# elif (bmi >= 18.5 and bmi < 24): # else if (判斷) : True and False = False
#     print("你很健康") 
# elif (bmi >= 24 and bmi < 27): # True and False = False
#     print("過重")
# elif (bmi >= 27 and bmi < 30): # True and True = True
#     print("輕度肥胖")
# elif (bmi >= 30 and bmi <= 35):
#     print("中度肥胖")
# elif (bmi >= 35):
#     print("重度肥胖")
# else:
#     print("你的數字可能有問題?")
# =============================================================================

# 改善 雙層if:如果使用者輸入的是數字才可以計算判斷 (tryExcept劣質版)
weight = input("請輸入你的體重(kg)")
height = input("請輸入你的身高(cm)")
print(f"{height}是身高, {weight}是體重")
## 算使用者的bmi: 體重/身高(m)平方
if (weight.isdigit() and height.isdigit()): # 判斷是否為數字 使用 函式 變數.isdigit() = True False
    weight = float(weight) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
    height = float(height) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
    bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
    print(f"BMI是{bmi:+5.2f}") # 偷偷看一下目前BMI是多少 把她print出來
    ## 目前bmi狀態
    if (0 < bmi < 18.5): # 0 < bmi < 18.5: 過輕
        print("體重過輕")
    elif (bmi >= 18.5 and bmi < 24): # else if (判斷) : True and False = False
        print("你很健康") 
    elif (bmi >= 24 and bmi < 27): # True and False = False
        print("過重")
    elif (bmi >= 27 and bmi < 30): # True and True = True
        print("輕度肥胖")
    elif (bmi >= 30 and bmi <= 35):
        print("中度肥胖")
    elif (bmi >= 35):
        print("重度肥胖")
    else:
        print("你的數字可能有問題?")
else:
    print("阿你這個根本不是數字吧!")        




