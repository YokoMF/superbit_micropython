# Copyright (c) 2019
# Author: wusicaijuan/陈帅气
# All rights reserved.
#
# Heavily based on
# https://github.com/adafruit/micropython-adafruit-pca9685/blob/master/pca9685.py
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import PCA9685
import math

enSoervo = (0, 1, 2, 3, 4, 5, 6, 7)


class Servos:
    def __init__(self, i2c, address=0x40, freq=50):
        self.pca9685 = PCA9685.PCA9685(i2c, address)
        self.pca9685.set_pwm_freq(freq)

    def Servo180(self, index, degree: int):
        us = float(degree*1800/180+600)
        pwm = float(us*4096/20000)
        self.pca9685.duty(enSoervo[index-1], int(pwm))

    def Servo270(self, index, degree: int):
        newdegree = degree/1.5
        us = float(newdegree*1800/180+600)
        pwm = float(us*4096/20000)
        self.pca9685.duty(enSoervo[index-1], int(pwm))

    def Servo360(self, index, pos: int, value):
        if pos == 1:
            us = float(90*1800/180+600)
            pwm = float(us*4096/20000)
            self.pca9685.duty(enSoervo[index-1], int(pwm))
        elif pos == 2:
            us = float((90-value)*1800/180+600)
            pwm = float(us*4096/20000)
            self.pca9685.duty(enSoervo[index-1], int(pwm))
        elif pos == 3:
            us = float((90+value)*1800/180+600)
            pwm = float(us*4096/20000)
            self.pca9685.duty(enSoervo[index-1], int(pwm))

    def release(self, index):
        self.pca9685.duty(index, 0)
