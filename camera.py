# 学习使用 pycharm 远程控制树莓派
# 环境：windows10 + pycharm2020 + 树莓派4b
# 代码来自https://www.jianshu.com/p/6644d4932136
# 参考博文《树莓派摄像头Camera的使用》，作者：羋虹光

from picamera import PiCamera
from time import sleep

# 使用 PiCamera 方法创建 camera 对象
camera = PiCamera()

# 旋转图像角度
# camera.rotation = 90

# 设置图片分辨率，图片最大分辨率位 2592*1944，视频最大分辨率位1920*1080
# 最低分辨率为 64*64
camera.resolution = (2592, 1944)
# 设置帧速率
camera.framerate = 15

# 相机预览
camera.start_preview()

# alpha参数设置透明度 0~255，值越小，图片越透明
# camera.start_preview(alpha = 255)

sleep(5)
# 拍摄静态图像并保存到指定路径，sleep至少2秒让相机感应光线
# camera.capture("/home/pi/Pictures/imag1.jpg")

# 循环拍摄3张静态图片
# for i in range(2, 5):
#     sleep(5)
#     camera.capture('/home/pi/Pictures/image%s.jpg' % i)

camera.stop_preview()