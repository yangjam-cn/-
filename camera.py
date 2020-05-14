# 学习使用 pycharm 远程控制树莓派
# 环境：windows10 + pycharm2020 + 树莓派4b
# 代码来自https://www.jianshu.com/p/6644d4932136
# 参考博文《树莓派摄像头Camera的使用》，作者：羋虹光

from picamera import PiCamera, Color
from time import sleep

# 使用 PiCamera 方法创建 camera 对象
camera = PiCamera()

# 旋转图像角度
# camera.rotation = 90

# 设置图片分辨率，图片最大分辨率位 2592*1944，视频最大分辨率位1920*1080
# 最低分辨率为 64*64
# camera.resolution = (2592, 1944)
# 设置帧速率
camera.framerate = 60

# 相机预览
camera.start_preview()

# alpha参数设置透明度 0~255，值越小，图片越透明
# camera.start_preview(alpha = 255)

# 向图像添加文本
# camera.annotate_text = "hello pi!"
# 设置文本大小
camera.annotate_text_size = 50
# 设置文本前后景颜色
# camera.annotate_background = Color('white')
# camera.annotate_foreground = Color('yellow')

# 设置预览图像亮度 0~100
camera.brightness = 60

# 循环增加图像亮度
# for i in range(100):
#     camera.annotate_text = "brightness = %s" % i
#     camera.brightness = i
#     sleep(0.1)

# 设置图像对比度 0~100
# for i in range(100):
#     camera.annotate_text = "contrast : %s" % i
#     camera.contrast = i
#     sleep(0.1)

# 设置图像特殊效果
# for effect in camera.IMAGE_EFFECTS:
#     camera.annotate_text = "effect: %s" % effect
#     camera.annotate_background = Color("white")
#     camera.annotate_foreground = Color("blue")
#     camera.image_effect = effect
#     sleep(2)
#     camera.capture("/home/pi/Pictures/%s.jpg" % effect)

# 设置曝光模式
# for exposure in camera.EXPOSURE_MODES:
#     camera.annotate_text = "exposure mode: %s" % exposure
#     camera.annotate_foreground = Color("blue")
#     camera.annotate_background = Color("white")
#     camera.exposure_mode = exposure
#     sleep(5)
#     camera.capture("/home/pi/Pictures/%s.jpg" % exposure)

# 设置白平衡模式
# for awb in camera.AWB_MODES:
#     camera.annotate_text = "awb mode: %s" % awb
#     camera.annotate_foreground = Color("blue")
#     camera.annotate_background = Color("white")
#     camera.awb_mode = awb
#     sleep(5)
#     camera.capture("/home/pi/Pictures/%s.jpg" % awb)


sleep(10)

# 拍摄静态图像并保存到指定路径，sleep至少2秒让相机感应光线
# camera.capture("/home/pi/Pictures/imag1.jpg")

# 循环拍摄3张静态图片
# for i in range(2, 5):
#     sleep(5)
#     camera.capture('/home/pi/Pictures/image%s.jpg' % i)

camera.stop_preview()