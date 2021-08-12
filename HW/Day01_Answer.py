# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:06:16 2021
@title : Day01回家功課 (老師的寫法)
@author: shannon
"""
# from datetime import date


# birthday = input("請輸入生日(ex. 2000/06/31)")
# year, month, day = [int(x) for x in birthday.split("/")]
# # validate the date
# try:
#     # 使用python內建的套件:來檢查日期就不用自己寫拉 :D
#     date(year,month,day)
#     if(month == 1):
#         if(day<=22) print("摩羯座")
#         if(day>=21)
# except: 
#     print("您輸入的日期有誤!")

# Q1: 使用者可以輸入月份，結果會輸出該月份春夏秋冬哪一個季節
# =============================================================================
# try:
#     month = int(input("請輸入月份 (ex. 1)"))
#     if(month >=3 and month <=5 ):
#         print(f'{month}月是在春天')
#     elif(month >=6 and month <= 8):
#         print(f'{month}月是在夏天')
#     elif(month >= 9 and month <= 11):
#         print(f'{month}月是在秋天')
#     elif(month ==12 or month == 1 or month == 2):
#         print(f'{month}月是在冬天')
#     else:
#         print("錯誤的範圍，請輸入1-12其中一個數字")
# except:
#     print("請輸入整數，請輸入1-12其中一個數字")
# 
# =============================================================================

# Q2: 可以讓使用者可以不斷地輸入出生在哪個月份，直到輸入q或Q為止，並且結果會輸出這些input中，最多人在哪個季節出生?

answer = {'春天':0, '夏天':0, '秋天':0, '冬天':0} #分別是春, 夏天, 秋天, 冬天
wrong = 0
while True:
    try:
        month = input("請輸入你在幾月出生 (ex. 1), 如果想退出請輸入 q 或 Q =>")
        if(month == 'q' or month == 'Q'):
            break
        month = int(month)
        if(month >=3 and month <=5 ):
            print(f'{month}月是在春天')
            answer['春天']+=1
        elif(month >=6 and month <= 8):
            print(f'{month}月是在夏天')
            answer['夏天']+=1
        elif(month >= 9 and month <= 11):
            print(f'{month}月是在秋天')
            answer['秋天']+=1
        elif(month ==12 or month == 1 or month == 2):
            print(f'{month}月是在冬天')
            answer['冬天']+=1
        else:
            wrong +=1
            print("錯誤的範圍，請輸入1-12其中一個數字")
    except:
        wrong +=1
        print("請輸入整數，請輸入1-12其中一個數字")
        continue
        
print(f"春天{answer['春天']}人出生")
print(f"夏天{answer['夏天']}人出生")
print(f"秋天{answer['秋天']}人出生")
print(f"冬天{answer['冬天']}人出生")
print(f"共輸錯{wrong}次")

# Q3: 可以讓老師先輸入班級人數(假設10人)，然後使用For迴圈讓老師輸入所有人的成績，輸入完之後可以告訴老師班級總分及平均(取小數點第二位)
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
# for i in scores:
#     total+= i
# 
# print("全班共有", number, '人')
# print("總分是: ", total)
# print(f"平均是: {total/len(scores):5.2f}")    
# =============================================================================















