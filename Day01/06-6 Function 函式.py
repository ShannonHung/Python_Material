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
world = "I am the king" # global variable 

def country():
    global world # 如果少了這個就會變成區域變數
    world = 'I am the queen' # 我想要在world後面新增文字: 
    print("這是在裡面=> ", world)

country()
print("這是外面=> ", world)

# BMI整理