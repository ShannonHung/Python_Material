# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:50:57 2021
@title: 06-4 for 迴圈 (for loop)
@author: shannon
"""

# 基本list Cart購物車 : 容器都可以使用for 一個個印出來
# =============================================================================
# cart = ('c', 'b', 'a')
# for i in cart: # in 後面要寫變數名稱 還是 原本樣子 Ex. (1,2,3) 也可以
#     print(i)
# 
# =============================================================================
# 基本的走訪字串, 集合, 字典 (還記得之前說過嗎? str也是容器的一種喔)

# =============================================================================
# name = "Shannon"
# print(type(name))
# for i in name:
#     print(i)
# =============================================================================
 

# 再試試看Dict: 只取Key
testdict = {'one': 1, 'two': 2, 'three':3}
for i in testdict:
    print(i)


# 再試試看Dict: 只取Value
testdict = {'one': 1, 'two': 2, 'three':3}
for i in testdict.values():
    print(i)

# 再試試看Dict: 同時 取Key 和 Value
testdict = {'one': 1, 'two': 2, 'three':3}
for item in testdict.keys():
    print(item)
    print(type(item))
    
for key, value in testdict.items():  # 'one': 1
    print(f"this is key => {key}, this is value => {value}")

    
# for迴圈: range使用方式 (一個input)


# for迴圈: range使用方式 (2個input)


# for迴圈: range使用方式 (3個input)


# for迴圈: 也可以用break, continue, for...else...


# 九九乘法表: 很基本


# 三角形: 老師都很愛教的用*印三角形 
# (課堂練習: 請幫我印出菱形)






# BMI 結合for的概念  計算平均 + 加入容器 (資料結構)



