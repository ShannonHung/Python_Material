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
    print("開始進入try")
    
    # ===========================TRY: START================================
    try:
        child = input("請輸入分子") # 不能先轉數字 因為有可能會輸入q 
        mom = input("請輸入分母") # 不能先轉數字 因為有可能會輸入q 
        if(child == 'q' or mom == 'q'): break
        if(child == '1'): raise ZeroDivisionError() # 強迫電腦 跳 特定錯誤 ， Exception 
    
        # 確定不是q之後，我們再把他轉成數字
        child = float(child) # 變數 str 轉換成 float小數點作為分子計算
        mom = float(mom) # 變數 str 轉換成 float小數點作為分母計算
        
        result = float(child) / float(mom) # 進行除法
        print(f"{child}/{mom} 答案是 {child/mom:5.2f}") # 印出解答
    # 抓到分母為0的錯誤
    except ZeroDivisionError as error: # 有想到的錯誤 放到 erro 變數 名稱自由改 錯誤訊息 放到erro
        print("欸!!!分母不能為0阿!!!") # 如果抓到分母為0的錯誤，就執行這裡
        print(error) # 如果抓到分母為0的錯誤，就執行這裡
    # 型態轉換的錯誤 str -> float | int ; 發生就 把錯誤放到e變數裡面
    except ValueError:  # 如果沒有as 變數 也沒差! 頂多就印不出來電腦的錯誤訊息 
        print("欸!!! 你要輸入數字阿!!!") # 型態轉換的錯誤 發生的話就執行這裡
        # print(e) # 型態轉換的錯誤 發生的話就執行這裡
    # 如果上面的except甚麼都抓不到 最極端的狀況就執行 這裡!!
    except: # 沒想到的錯誤  
        print("好像有問題喔?!") # 上面except以外的錯誤 發生的話就執行這裡
    else: # 完全沒有任和錯誤就會執行
        print("wow!!! 完全沒有錯誤!")
    finally:  # 不管怎麼樣 有錯沒錯 都會執行
        print("無論怎麼樣都會執行")
    # ===========================TRY: END================================

    print("Try結束") # not part of try except，所以不會被上面的例外影響 我走我的路  


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
# 
# =============================================================================





