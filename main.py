import cv2
import numpy as np
import pygetwindow as gw
import pygame
import time

# 创建一个VideoCapture对象，参数0表示使用默认的摄像头
cap = cv2.VideoCapture(0)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("doorbell.mp3")
    pygame.mixer.music.play()

def draw_button(frame):
    cv2.rectangle(frame, (20, 20), (220, 80), (125, 170, 205), -1)
    cv2.putText(frame, 'DoorBell', (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        if 20 < x < 220 and 20 < y < 80:
            play_sound()

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Camera', mouse_event)

while True:
    # 从摄像头读取帧
    ret, frame = cap.read()

    if not ret:
        break

    # 检查窗口是否关闭
    if not gw.getWindowsWithTitle('Camera'):
        break

    # 获取窗口大小
    win = gw.getWindowsWithTitle('Camera')[0]
    width, height = win.size

    # 重设帧大小以适应窗口
    frame = cv2.resize(frame, (width, height))

    # 绘制按钮
    draw_button(frame)

    # 显示帧
    cv2.imshow('Camera', frame)

    # 按下q键时，退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
