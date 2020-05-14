# 使用 pycharm 远程控制树莓派实验
# 环境：windows10 + pycharm2020 + 树莓派4b

from picamera import PiCamera
from time import sleep

#
camera = PiCamera()

# 相机预览
camera.start_preview()
sleep(10)
camera.stop_preview()