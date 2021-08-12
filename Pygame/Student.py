# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 01:03:11 2021

@author: yourname
"""
import pygame
import time
from random import randint
# 螢幕尺寸
SCREEN_WIDTH = 400 #畫面寬度
SCREEN_HEIGHT = 400 #畫面高度

# 顏色
GREEN = (73, 188, 11) # 背景顏色 RGB
WHITE = (255, 255, 255) # 字體顏色

# game state: 0 - welcome, 1 - playing, 2 - game over
state = 0 # 控制現在哪個畫面 0 1 2 

# 建立視窗及載入圖片
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() # 計時要用的
mole = pygame.image.load('mole.png') # 老鼠圖案
mallet = pygame.image.load('mallet.png') # 槌子圖案

# pygame.mouse.set_visible(False)
pygame.display.set_caption('click a mole') # 遊戲標題
pygame.font.init() #文字初始化

x = None
y = None
score = 0
game_time = 10 # 調時間
start_time = 0
mallet_down = False

clock = pygame.time.Clock()
background = pygame.image.load('grass.png')
down_mallet = pygame.image.load('down-mallet.png')

## 這是第一個畫面

def welcome_screen():
    # 背景填滿綠色
    screen.fill(GREEN)
    # 設定字體樣板
    font = pygame.font.Font(None, 30)
    # 設定文字
    text = font.render("press ENTER to start", False, WHITE)
    # 將文字、老鼠及槌子顯示在畫面上
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 185))
    screen.blit(mallet, (200, 50))
    screen.blit(mole, (120, 250))

## 這是第二個畫面
def play_screen():
    # 將草地顯示在背景上
    screen.blit(background, (0,0))
    # 顯示時間
    show_timer()
    show_score() 
    show_mole() 
    show_mallet() 

def show_mole():
    # 把隨機出來的位置放老鼠上去
    screen.blit(mole, (x, y))  #這時候的x, y已經更新過了
def show_mallet():
    # 檢查槌子狀態
    check_mallet_state()
    # 取得槌子圖片各種位置資料
    mallet_position = mallet.get_rect()
    # 將槌子的中心點設在滑鼠點的位置
    mallet_position.center = pygame.mouse.get_pos()
    # 依照狀態不同將槌子顯示
    if mallet_down:
        # 如果mallet_down滑鼠是點下的狀態True-塞槌子槌下去的圖片
        screen.blit(down_mallet, mallet_position)
    else:
        # 如果mallet_down滑鼠是點下的狀態False-塞槌子原始的圖片
        screen.blit(mallet, mallet_position)  
def show_score():
    # 設定字型模板
    font = pygame.font.Font(None, 28)
    # 用模板來建立分數文字
    text = font.render(str(score), False, WHITE)
    # 將文字顯示上去
    screen.blit(text, (10, 0))

def check_mallet_state():
    global mallet_down
    # 檢查滑鼠左鍵有沒有被按，[左鍵、中鍵、右鍵]，如果被按下則為 True，[0]為抓到左鍵是否為True表示被按下去。
    if pygame.mouse.get_pressed()[0]:
        mallet_down = True # 改變狀態: 鎚子槌下去
    else:
        mallet_down = False # 改變狀態: 槌子恢復原本樣貌

## 這是第三個畫面
def end_screen():
    # 背景填滿綠色
    screen.fill(GREEN)
    font = pygame.font.Font(None, 30)
    # text = font.render("END", False, WHITE) 😀# TODO 註解
    # screen.blit(text, (100,200)) 😀#TODO 註解
    #==================TODO 1: START========================
    game_over = font.render("GAME OVER", False, WHITE)
    font = pygame.font.Font(None, 25)
    points = font.render("score: " + str(score), False, WHITE)
    font = pygame.font.Font(None, 22)
    restart = font.render("press ENTER to play again", False, WHITE)
    # 將上述資訊顯示到螢幕上
    screen.blit(game_over, (SCREEN_WIDTH / 2 - game_over.get_width() / 2, 100))
    screen.blit(points, (SCREEN_WIDTH / 2 - points.get_width() / 2, 200))
    screen.blit(restart, (SCREEN_WIDTH / 2 - restart.get_width() / 2, 300))   
    
def show_timer():
    # 現在的時間 - 開始時間 = 經過的秒數
    elapsed = time.time() - start_time
    # 遊戲總時間 - 經過的秒數 = 要顯示的剩餘秒數
    timer = game_time - elapsed
    # 如果秒數歸零則遊戲結束
    if timer < 0:
        end()
    # 建立字型模板、建立時間文字及顯示到畫面上
    font = pygame.font.Font(None, 28)
    text = font.render(str(int(timer)), False, WHITE)
    screen.blit(text, (370, 0))


def end():
    # 狀態改為 2 結束遊戲
    global state
    state = 2 # state = 0 welcome , 1 = playing, 2 = end 

def play():
    # 取用遊戲狀態、分數及開始時間資訊
    global state, score, start_time
    # 設定遊戲開始時間 time.time() 會取得目前的時間
    start_time = time.time()
    # 將分數歸 0 且狀態設定為 1 遊玩中
    score = 0
    state = 1
    # 產生新的老鼠（這邊先立一個函式之後完成）
    new_mole()
    # 產生瞬間先檢查是否有被打到（這邊先立一個函式之後完成）
    whack()

def new_mole():
    # 隨機決定下一個老鼠產生的位置
    global x, y
    # x 從螢幕最左到右邊 扣掉老鼠的寬都能取, y 則向下移 30 到底部扣掉老鼠的高都能取
    x = randint(0, SCREEN_WIDTH - mole.get_width())
    y = randint(30, SCREEN_HEIGHT - mole.get_height())
def whack():
    global score
    # 取得滑鼠當前的位置
    mx, my = pygame.mouse.get_pos()
    # 取得老鼠的寬及高
    width, height = mole.get_size()
    # 將座標計算是不是點擊在老鼠的圖片上, 如果有的話要加分和產生下一隻新的
    # mx-x 是滑鼠與老鼠圓心的距離 要小於等於<= 老鼠1/2寬度width/2
    if abs(mx - x - width / 2) <= width / 2 and abs(my - y - height / 2) <= height / 2:
        score += 1 
        new_mole()    
    
# 處理首頁
def handle_welcome(e):
    # 顯示歡迎畫面
    welcome_screen()
    # 偵測鍵盤 Enter 事件
    if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
        play()
        

def handle_play(e):
    # 偵測滑鼠按下事件
    if e.type == pygame.MOUSEBUTTONDOWN:
        whack() # 檢查有沒有打到老鼠

def handle_end(e):
    # 偵測鍵盤 Enter 事件
    if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
        play()
        
# 遊戲主要運行的流程
def main():
    # 設定運行狀態
    running = True
    while running:
        # 使用了pygame.event.get()來處理所有的事件
        for event in pygame.event.get():
            # 當按下視窗的 X 結束遊戲運行
            if event.type == pygame.QUIT:
                running = False
            # 首頁
            elif state == 0:
                # welcome_screen()
                handle_welcome(event) # 
        #     # 遊玩中
            elif state == 1:
                handle_play(event)
        #     # 遊戲結束
            elif state == 2:
                handle_end(event)

        # # 遊玩中繪製遊戲畫面
        if state == 1:
            play_screen()
        # # 結束時繪製結束畫面
        if state == 2:
            end_screen()

        # 設定每秒至少 update 30 次 (對這個 while loop) 表示每秒最多應通過30幀
        # clock.tick(30)

        # 更新畫面
        pygame.display.update()

    # 當視窗關閉時 (running = false), 關閉視窗
    pygame.quit()


# 執行遊戲主要運行流程
main()

