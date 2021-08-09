# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 00:23:18 2021
@title : 06-5 Exception 例外處理
@author: shannon
"""
# TraceBack: 追朔程式呼叫的歷程 (會讓程式停止 如果沒tryExcept)


# try...except...避免因為發生例外而被終止: (即使發生例外也不會讓程式停止)
    # 你可以發現try...catch...可以讓程式正常的印出print me please!


# 捕捉特定的例外 except 特定例外類型 as 變數名稱:

    
# (承上題)try...except...else...finally...


# BMI 改寫原本的code: 加入try...catch...
classroom = {}
while True:    
    name = input("請輸入名稱(name)")
    weight = input("請輸入體重 (kg)")
    height = input("請輸入身高 (cm)")
    # TODO: if使用try...Except來代替
    if(weight.isdigit() and height.isdigit()): 
        bmi = float(weight) / (float(height)/100)**2 
        print(f"您的BMI為:{bmi:5.2f}\n")
        classroom[name] = bmi
        if bmi < 18.5:
            print("嘿!你太輕了!")
        elif bmi >= 18.5 and bmi < 24:
            print("健康")
        elif bmi >= 24 and bmi < 27:
            print("過重")
        elif bmi >= 27 and bmi < 30: 
            print("輕度肥胖")
        elif bmi >= 30 and bmi <= 35:
            print("中度肥胖")
        elif bmi >= 35:
            print("重度肥胖")
        else:
            print("你輸入的數值有問題!")
    # TODO: 使用except替代
    else:
        print("請輸入數字!!")
    
    status = input("是否要計算BMI (yes輸入y, no 輸入任意鍵)?")
    if (status == 'Y' or status == 'y'): 
        continue
    else:
        break

total = 0
# TODO: 使用tryExcept替代
for thisKey, thisValue in classroom.items():
    print(thisKey, " <= key, value => ", thisValue)
    total += thisValue
total /= len(classroom)
print("全班BMI平均: ", total)
print(f"全班BMI平均:{total:5.2f}")







