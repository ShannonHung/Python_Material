# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 00:23:18 2021
@title : 06-5 Exception 例外處理
@author: shannon
"""
# =============================================================================
# int('five')
# print("hello")
# =============================================================================

# try 通常用在可能會發生錯誤的地方 try catch try except
# try...except...避免因為發生例外而被終止: (即使發生例外也不會讓程式停止)

##  =========有try except 差別 =========
# =============================================================================
# a = 1
# b = 0
# # 世界1 : 噴錯 try except
# try:
#     print(a/b) # 噴錯 到 except 那邊去執行
#     print("我是try的一份子") # 這裡不會執行
# except: # 任何錯誤就會給他
#     print("我發現錯誤!!! 完蛋惹!! 但是沒關係!! 不會有紅紅") 
#     
# # 世界2: 不會世界1的錯誤影響，因為世界1被try except 包住了，交給他們處理就對了 
# print("你好!!!")
# print("hello!!!")
# =============================================================================

## =========沒有try except的差別=========
# =============================================================================
# a = 1
# b = 0
# print(a/b)
# print("我發現錯誤!!! 完蛋惹!! 但是沒關係!! 不會有紅紅") 
# print("你好!!!")
# print("hello!!!")
# =============================================================================


# 捕捉特定的例外 except 特定例外類型 as 變數名稱: Ex. except ZeroDivisionError as e:
while True:
    
    try:
        child = input("請輸入分子")
        mom = input("請輸入分母")
        if(child == 'q' or mom == 'q'): break
        
    #把child 跟 mom 轉成數字，因為沒有要quit退出
        child = float(child)
        mom = float(mom)
        
        result = float(child) / float(mom)
        print(f"{child}/{mom} 答案是 {child/mom:5.2f}")
        
    except ZeroDivisionError as erro: # 有想到的錯誤 放到 erro 變數 名稱自由改 錯誤訊息 放到erro
        print("欸!!!分母不能為0阿!!!")
        print(erro)
        
    except ValueError as e:  # 有想到的錯誤
        print("欸!!! 你要輸入數字阿!!!")
        print(e)
        
    except: # 沒想到的錯誤 
        print("好像有問題喔?!")


# child = float(input("請輸入分子"))
# mom = float(input("請輸入分母"))
# result = child / mom
# print(f"{child}/{mom} 答案是 {child / mom:5.2f}") 






# BMI 改寫原本的code: 加入try...catch... # try ... except 就是要把可能 出現問題的地方包起來!!
# =============================================================================
# number = float(input("請輸入你要測幾次bmi=>")) # 10
# count = 0.0
# while True:
#     print("開始跑")
#     # bmi
#     try:
#         weight = float(input("請輸入你的體重(kg)"))
#         height = float(input("請輸入你的身高(cm)"))
#         print(f"{height}是身高, {weight}是體重")
#         ## 算使用者的bmi: 體重/身高(m)平方
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
#     except:
#         print("QAQ有錯誤!!")
#         continue 
#     
#     count = count + 1 # 目前跑的次數 會一直+1
#     if(number == count):# count == number 目前的次數跟 使用者希望跑的次數有沒有一樣
#         break
#     else:
#         continue
#     # (count += 1) equal to (count = count + 1)
# =============================================================================






