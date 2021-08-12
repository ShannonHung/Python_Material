# -*- coding: utf-8 -*-
"""
@author: '第O組_OOO'
按 ctrl + 5 解開註解
"""
# CTRL+ F 搜尋
# Q3: 可以讓老師先輸入班級人數(假設10人)，然後使用For迴圈讓老師輸入所有人的成績，輸入完之後可以告訴老師班級總分及平均(取小數點第二位)
number = int(input("請輸入班級人數:")) # 班級人數 = 迴圈跑的次數
scores = [] # 放所有正確成績的地方
total = 0 # 總分
count = 0 # 輸入成功成績的次數

# DONE: While 或是 for迴圈可以讓使用者輸入正確的分數{number變數}次 number == count
while (count != number):# 如果 正確的次數 還沒達到 班級人數 就要繼續做
    # DONE: try...except...抓到使用者成績異常輸入
    try:
        score = float(input("請輸入成績")) # DONE3 : 使用者輸入成績 50
        if(score >= 0 and score <= 100):
            count +=1 
            scores.append(score)
        else:
        # DONE: 如果判斷成績錯誤就重新輸入一次
            print("成績請輸入0-100之間，請重新輸入")
            continue
            # DONE: 迴圈重新輸入
    # DONE: try...except...抓到使用者成績異常輸入
    except:
        print("成績異常請重新輸入")
        continue
        # DONE: 成績異常迴圈重新輸入

# DONE: 將scores裡面每個成績加總
# total  = sum(scores)
for i in scores:
    total = total + i

print("全班共有", number, '人')
print("總分是: ", total)
print(f"平均是: {total/len(scores):5.2f}")    
