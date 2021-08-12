# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:30:32 2021
@title: 2-1 Function
@author: shannon
"""
# function的基本寫法: f(x,y) = x**2 + y**2; def 名稱(參數):
# =============================================================================
# def f(x=0, y=0): # 你可以填預設值
#     print(f"x => {x}, y=>{y}")
#     return x**2 + y**2 # **平方，return 會丟給呼叫函式名稱function name 的地方
# y = f(1) # 5 => y = 5 這裡呼叫函式，Return 會丟給y
# print(y) # 把y給印出來
# 
# 
# def f(x, y): # 如果沒有預設值，就會出錯!
#     print(f"x => {x}, y=>{y}")
#     return x**2 + y**2 # **平方，return 會丟給呼叫函式名稱function name 的地方
# y = f(1) # 5 => y = 5 這裡呼叫函式，Return 會丟給y
# print(y) # 把y給印出來
# =============================================================================

# 一個參數: 計算1-10的圓面積
# =============================================================================
# def circleArea(r):
#     print("function裡面的r =>",r)
#     return r ** 2 * 3.1415926
# 
# for i in range(1,11,1):
#     print(f"半徑為{i}長度的圓面積為 => {i}")
# 
# =============================================================================

# 非數字: str
# =============================================================================
# def thankyou(name ="OOO", yourName="我"): 
#     print("您好" , name , yourName , "歡迎您下次再來!") 
#     # /n就是下一行的意思
#     words ="您好" + name + yourName + "歡迎您下次再來!" + "\n" + "    敬上"
#     return words # 不一定要return; 也可以不寫return
# 
# yourName = "shannon"
# thankyou("小美", yourName)
# print(thankyou())
# =============================================================================

# 容器物件: list, set, tuple, dict (隨意容器的總和) 
# =============================================================================
# classB = [10,9,5,8]
# 
# def score_Sum(allpeople = []):
#     total = 0
#     for i in allpeople:
#         print("目前的數字 =>", i)
#         total = total + i
#         print("加總結束 \n 跑下一個迴圈loop \n ")
#     return total
# 
# print("ClassA的總分", score_Sum([100,90,50,80]))
# print("ClassB的總分", score_Sum(classB))
# 
# =============================================================================

# 變數的有效範圍 Scope Rule: PPT
# =============================================================================
# world = "I am the king" # global variable 
# 
# def country():
#     # 加上global就會改同一個人; 沒有加上去就不會改同一個人，會自己建立一個
#     global world # 如果少了這個就會變成區域變數, 注意: 不要寫global world = "做事"
#     world = 'I am the queen' # 我想要在world後面新增文字: 
#     print("這是在裡面=> ", world)
# 
# country()
# print("這是外面=> ", world)
# =============================================================================

# BMI整理之前
number = float(input("請輸入你要測幾次bmi=>")) # 10
count = 0.0
while True:
    print("開始跑")
    # bmi
    try:
        weight = float(input("請輸入你的體重(kg)"))
        height = float(input("請輸入你的身高(cm)"))
        print(f"{height}是身高, {weight}是體重")
        ## 算使用者的bmi: 體重/身高(m)平方
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
    except:
        print("QAQ有錯誤!!")
        continue 
    
    count = count + 1 # 目前跑的次數 會一直+1
    if(number == count):# count == number 目前的次數跟 使用者希望跑的次數有沒有一樣
        break
    else:
        continue
    # (count += 1) equal to (count = count + 1)




# BMI整理之後
number = float(input("請輸入你要測幾次bmi=>")) # 10
count = 0.0
weight = 0.0
height = 0.0
bmi = 0.0 

# 通常函式寫在 主程式上面 | 下面
# =====Part1: 輸入使用者資料 並且轉成數字==== 
def userInputToInt(): 
    # local varaibe　區域
    global weight, height
    weight = float(input("請輸入你的體重(kg)"))
    height = float(input("請輸入你的身高(cm)"))
    print(f"{height}是身高, {weight}是體重")
    ## 算使用者的bmi: 體重/身高(m)平方
    weight = float(weight) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
    height = float(height) # 如果是True發現是數字，我才會開始計算BMI然後把變數轉成數字
        
# ====Part2: 計算BMI====
def calculateBMI():
    global bmi 
    bmi = weight / ((height/100) ** 2) # pow((height/100), 2)
    print(f"BMI是{bmi:+5.2f}") # 偷偷看一下目前BMI是多少 把她print出來
        
## ====Part3: 判斷BMI====
def valuateBMI():
    global bmi 
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
        userInputToInt() # Part1: 輸入使用者資料
        calculateBMI() # Part2: 計算BMI
        valuateBMI() # Part3: 判斷BMI
    except:
        print("QAQ有錯誤!!")
        continue 
    # 目前跑的次數 會一直+1
    count = count + 1 
    # count == number 目前的次數跟 使用者希望跑的次數有沒有一樣
    if(number == count): break
    else: continue












