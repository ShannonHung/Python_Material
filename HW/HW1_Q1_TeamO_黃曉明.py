# -*- coding: utf-8 -*-
"""
@author: '第O組_OOO'
按 ctrl + 5 解開註解
"""

# Q1: 使用者可以輸入月份，結果會輸出該月份春夏秋冬哪一個季節
try:
    month = int(input("請輸入月份")) # int() float()
    if(month >= 3 and month <= 5):
        print(f'{month}月是在春天')
        # TODO4: 秋天, 夏天, 冬天也是跟春天一樣的步驟
    elif(month >= 6 and month <= 8):
        print(f'{month}月是在夏天')
    elif(month >= 9 and month <= 11):
        print(f'{month}月是在秋天')
    # 12 1 2 冬天
    elif(month == 1 or month == 2 or month == 12):   
        print(f'{month}月是在冬天')
    else:
        print("錯誤的範圍，請輸入1-12其中一個數字")
    # TODO5: 如果月份不是在1-12印出下列錯誤
    
except:
    print("請輸入數字!!這不是數字!!!，請輸入1-12其中一個數字")



