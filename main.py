import cv2
import numpy as np
import tkinter as tk
import PIL.Image, PIL.ImageTk

# 创建一个VideoCapture对象，参数0表示使用默认的摄像头
cap = cv2.VideoCapture(0)

# 获取摄像头的宽度和高度
ret, frame = cap.read()
height, width, _ = frame.shape
aspect_ratio = width / height

# 创建一个Tkinter窗口
root = tk.Tk()

# 创建一个Canvas用于显示图像
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()

while True:
    # 从摄像头读取帧
    ret, frame = cap.read()

    if not ret:
        break

    # 将OpenCV图像转换为Tkinter图像
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))

    # 在Canvas上绘制图像
    canvas.create_image(0, 0, anchor = tk.NW, image = frame)

    # 更新窗口尺寸
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    if window_width / window_height != aspect_ratio:
        # 保持宽高比不变
        window_height = window_width / aspect_ratio
        root.geometry("%dx%d" % (window_width, int(window_height)))

    # 更新Tkinter窗口
    root.update()

cap.release()
