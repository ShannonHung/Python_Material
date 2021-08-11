# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:50:09 2021
@title: 06-3 While迴圈
@author: shannon
"""

# while 簡單用法
# =============================================================================
# a = 1
# 
# while (a < 10): # True while做事了
#     print("hello 我是while的一份子") # 子民 做事
#     a = a + 5
# 
# print("我不是while的一份子") # 跳出
# =============================================================================


# 改善2 : 可以不斷的重複輸入 with while
# =============================================================================
# status = input("是否要計算BMI? (yes請輸入y, no請按任意鍵)") 
# print(status)
# while (status=='y' or status=='Y'):
#     print("計算BMI開始...") 
#     # BMI ....
#     print("計算BMI結束!!") 
#     status = input("是否要計算BMI? (yes請輸入y, no請按任意鍵)") 
# 
# print("謝謝惠顧~ 請下次再來~")
# =============================================================================

# =============================================================================
# while True: # True 沒啥決定權
#     print("計算BMI開始...") 
#     # Tab => 整體往前四格 , Shift+Tab => 整體往後四格
#     weight = input("請輸入你的體重(kg)")
#     height = input("請輸入你的身高(cm)")
#     print(f"{height}是身高, {weight}是體重")
#     ## 算使用者的bmi: 體重/身高(m)平方
#     if (weight.isdigit() and height.isdigit()): # 判斷是否為數字 使用 函式 變數.isdigit() = True False
#         weight = float(weight) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
#         height = float(height) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
#         bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
#         print(f"BMI是{bmi:+5.2f}") # 偷偷看一下目前BMI是多少 把她print出來
#         ## 目前bmi狀態
#         if (0 < bmi < 18.5): # 0 < bmi < 18.5: 過輕
#             print("體重過輕")
#         elif (bmi >= 18.5 and bmi < 24): # else if (判斷) : True and False = False
#             print("你很健康") 
#         elif (bmi >= 24 and bmi < 27): # True and False = False
#             print("過重")
#         elif (bmi >= 27 and bmi < 30): # True and True = True
#             print("輕度肥胖")
#         elif (bmi >= 30 and bmi <= 35):
#             print("中度肥胖")
#         elif (bmi >= 35):
#             print("重度肥胖")
#         else:
#             print("你的數字可能有問題?")
#     else:
#         print("阿你這個根本不是數字吧!")        
# 
#     print("計算BMI結束!!") 
#     status = input("是否要計算BMI? (yes請輸入y, no請按任意鍵)") 
#     if(status == 'y' or status =='Y'): # while 子民決定: if 
#         continue # continue => 重作 
#     else: # break => 不做
#         break
# 
# print("謝謝惠顧~ 請下次再來~")
# =============================================================================

number = float(input("請輸入你要測幾次bmi=>")) # 10
count = 0.0
while True:
    print("開始跑")
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
    print("跑完")
    count = count + 1 # 目前跑的次數 會一直+1
    if(number == count):# count == number 目前的次數跟 使用者希望跑的次數有沒有一樣
        break
    else:
        continue
    # (count += 1) equal to (count = count + 1)

# while True: # True 沒啥決定權
#     print("計算BMI開始...") 
#     # Tab => 整體往前四格 , Shift+Tab => 整體往後四格
#     weight = input("請輸入你的體重(kg)")
#     height = input("請輸入你的身高(cm)")
#     print(f"{height}是身高, {weight}是體重")
# #     ## 算使用者的bmi: 體重/身高(m)平方
#     if (weight.isdigit() and height.isdigit()): # 判斷是否為數字 使用 函式 變數.isdigit() = True False
#         weight = float(weight) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
#         height = float(height) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
#         bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
#         print(f"BMI是{bmi:+5.2f}") # 偷偷看一下目前BMI是多少 把她print出來
#         ## 目前bmi狀態
#         if (0 < bmi < 18.5): # 0 < bmi < 18.5: 過輕
#             print("體重過輕")
#         elif (bmi >= 18.5 and bmi < 24): # else if (判斷) : True and False = False
#             print("你很健康") 
#         elif (bmi >= 24 and bmi < 27): # True and False = False
#             print("過重")
#         elif (bmi >= 27 and bmi < 30): # True and True = True
#             print("輕度肥胖")
#         elif (bmi >= 30 and bmi <= 35):
#             print("中度肥胖")
#         elif (bmi >= 35):
#             print("重度肥胖")
#         else:
#             print("你的數字可能有問題?")
#     else:
#         print("阿你這個根本不是數字吧!")        

#     print("計算BMI結束!!") 
#     status = input("是否要計算BMI? (yes請輸入y, no請按任意鍵)") 
#     if(status == 'y' or status =='Y'): # while 子民決定: if 
#         continue # continue => 重作 
#     else: # break => 不做
#         break

# print("謝謝惠顧~ 請下次再來~")



    
# 改進3: while 搭配 break, continue
        

 

