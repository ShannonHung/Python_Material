# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:27:36 2021

@author: shannon
"""

number = float(input("請輸入你要測幾次bmi=>")) # 10
count = 0.0
weight = 0.0
height = 0.0
bmi = 0.0 
 
def Part1():
    # 把外面的weight 跟 height請進來
    global weight
    global height
    weight = float(input("請輸入你的體重(kg)"))
    height = float(input("請輸入你的身高(cm)"))
    print(f"{height}是身高, {weight}是體重")
    ## 算使用者的bmi: 體重/身高(m)平方
    weight = float(weight) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
    height = float(height) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
        
def Part2():
    global bmi 
    bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
    print(f"BMI是{bmi:+5.2f}") # 偷偷看一下目前BMI是多少 把她print出來
    
def Part3():
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
    
while True:
    print("開始跑")
    # bmi
    try:
        # Part1 : 輸入內容 然後 轉成數字
        Part1()
        # Part2: 計算
        Part2()
        # Part3: 判斷
        Part3()
    except:
        print("QAQ有錯誤!!")
        continue 
    
    count = count + 1 # 目前跑的次數 會一直+1
    if(number == count):# count == number 目前的次數跟 使用者希望跑的次數有沒有一樣
        break
    else:
        continue
    # (count += 1) equal to (count = count + 1)
