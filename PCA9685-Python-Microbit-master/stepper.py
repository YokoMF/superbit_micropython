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
from microbit import sleep
import PCA9685

STP_CHA_L = 2047
STP_CHA_H = 4095

STP_CHB_L = 1
STP_CHB_H = 2047

STP_CHC_L = 1023
STP_CHC_H = 3071

STP_CHD_L = 3071
STP_CHD_H = 1023

enSteppers = (0x1, 0x2)

# 1/4 = 90°
# 1/2 = 180°
# 1 = 360°
# 2 = 720°
# 3 = 1080°
# 4 = 1440°
# 5 = 1800°
enTurns = (90, 180, 360, 720, 1080, 1440, 1800)


class Steppers:
    def __init__(self, i2c, address=0x40, freq=50):
        self.pca9685 = PCA9685.PCA9685(i2c, address)
        self.pca9685.set_pwm_freq(freq)

    def setStepper(self, index, dir: bool):
        if index == 0x1:
            if dir:
                self.pca9685.set_pwm(11, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(9, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(10, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(8, STP_CHD_L, STP_CHD_H)
            else:
                self.pca9685.set_pwm(8, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(10, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(9, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(11, STP_CHD_L, STP_CHD_H)
        else:
            if dir:
                self.pca9685.set_pwm(12, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(14, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(13, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(15, STP_CHD_L, STP_CHD_H)
            else:
                self.pca9685.set_pwm(15, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(13, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(14, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(12, STP_CHD_L, STP_CHD_H)

    # * Function      StepperDegree(index, degree)
    # * @author       wusicaijuan
    # * @date         2019.06.22
    # * @bried        步进电机转动角度
    # * @param[in1]   index
    #                     1: B1
    #                     2: B2
    # * @param[in2]   degree
    #                     degree > 0 : forward
    #                     degree < 0 : reverse
    # * @retval       void

    def StepperDegree(self, index, degree):
        self.setStepper(enSteppers[index-1], degree > 0)
        degree = abs(degree)
        sleep(10240 * degree / 360)
        self.pca9685.set_pwm(11, 0, 0)
        self.pca9685.set_pwm(9, 0, 0)
        self.pca9685.set_pwm(10, 0, 0)
        self.pca9685.set_pwm(8, 0, 0)
        self.pca9685.set_pwm(12, 0, 0)
        self.pca9685.set_pwm(14, 0, 0)
        self.pca9685.set_pwm(13, 0, 0)
        self.pca9685.set_pwm(15, 0, 0)

    # * Function      StepperTurn(index, turn)
    # * @author       wusicaijuan
    # * @date         2019.06.22
    # * @bried        步进电机转动圈数
    # * @param[in1]   index
    #                     1: B1
    #                     2: B2
    # * @param[in2]   turn : forward
    #                     1: 90(1/4turn)
    #                     2: 180(1/2turn)
    #                     3: 360(1turn)
    #                     4: 720(2turn)
    #                     5: 1080(3turn)
    #                     6: 1440(4turn)
    #                     7: 1800(5turn)
    # * @retval       void

    def StepperTurn(self, index, turn):
        degree = enTurns[turn-1]
        self.StepperDegree(enSteppers[index-1], degree)
