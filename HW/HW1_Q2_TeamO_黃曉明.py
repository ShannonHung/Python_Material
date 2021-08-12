# -*- coding: utf-8 -*-
"""
@author: '第O組_OOO'
按 ctrl + 5 解開註解
"""

# Q2: 可以讓使用者可以不斷地輸入出生在哪個月份，直到輸入q或Q為止，並且結果會輸出這些input中，最多人在哪個季節出生?

answer = {'春天':0, '夏天':0, '秋天':0, '冬天':0} #分別是春, 夏天, 秋天, 冬天
wrong = 0 # 錯誤累積次數 
while True:
    try:
        month = input("請輸入你在幾月出生 (ex. 1), 如果想退出請輸入 q 或 Q =>")
        # TODO: 如果輸入q或是Q就退出 

            
        # TODO: 因為要進行數字比較，請轉成int
        if(# TODO: 判斷month是否在3-5):
            print(f'{month}月是在春天')
            # TODO: 春天的次數+1 
        # TODO: 夏天, 秋天, 冬天都是類似跟春天差不多作法
  
        # TODO: 如果使用者不是輸入1-12月就顯示以下錯誤
            # TODO: 錯誤累計次數+1次
            print("錯誤的範圍，請輸入1-12其中一個數字")
    except:
        print("請輸入整數，請輸入1-12其中一個數字")
        # TODO: 如果輸入非整數內容，錯誤累計次數+1次並且重新輸入
        
print(f"春天{answer['春天']}人出生")
print(f"夏天{answer['夏天']}人出生")
print(f"秋天{answer['秋天']}人出生")
print(f"冬天{answer['冬天']}人出生")
print(f"共輸錯{wrong}次")
