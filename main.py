import cv2
import numpy as np

# 创建一个VideoCapture对象，参数0表示使用默认的摄像头
cap = cv2.VideoCapture(0)

# 检查是否成功打开摄像头
if not cap.isOpened():
    # 创建一个空窗口，标题为“无可用摄像头”
    cv2.namedWindow("无可用摄像头", cv2.WINDOW_NORMAL)
    while True:
        # 显示一个黑色画面
        cv2.imshow("无可用摄像头", np.zeros((480, 640), dtype=np.uint8))
        # 按下q键时，退出循环
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
else:
    cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    while True:
        # 从摄像头读取帧
        ret, frame = cap.read()

        if not ret:
            break

        # 显示帧
        cv2.imshow('Camera', frame)

        # 按下q键时，退出循环
        if cv2.waitKey(1) == ord('q'):
            break

    # 释放摄像头资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()
