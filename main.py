import cv2

# 创建一个VideoCapture对象，参数0表示使用默认的摄像头
cap = cv2.VideoCapture(0)

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
