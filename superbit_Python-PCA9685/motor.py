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

# M1 : 8. 9
# M2 : 10, 11
# M3 : 12, 13
# M4 : 14, 15
enMotors = (8, 10, 12, 14)

class DCMotors:
    def __init__(self, i2c, address=0x40, freq=50):
        self.pca9685 = PCA9685.PCA9685(i2c, address)
        self.pca9685.set_pwm_freq(freq)


    # * Function      MotorRun(index, speed)
    # * @author       wusicaijuan
    # * @date         2019.06.22
    # * @bried        控制某一直流电机，调节速度
	# 					Control a DC motor, adjust the speed
    # * @param[in1]   index
    #                     1: M1
    #                     2: M2
    #                     3: M3
    #                     4: M4
    # * @param[in2]   speed
    #                     speed > 0 : forward
    #                     speed < 0 : reverse
    # * @retval       void
    def MotorRun(self, index, speed):
        a = enMotors[index - 1]
        b = a + 1
        speed = speed * 16  # map 255 to 4096
        if speed > 4096:
            speed = 4095
        if speed < -4096:
            speed = -4095

        if a > 10:
            if speed >= 0:
                self.pca9685.set_pwm(a, 0, speed)
                self.pca9685.set_pwm(b, 0, 0)
            else:
                self.pca9685.set_pwm(a, 0, 0)
                self.pca9685.set_pwm(b, 0, -speed)
        else:
            if speed >= 0:
                self.pca9685.set_pwm(a, 0, speed)
                self.pca9685.set_pwm(b, 0, 0)
            else:
                self.pca9685.set_pwm(a, 0, 0)
                self.pca9685.set_pwm(b, 0, -speed)


    # * Function      stopMotor(index)
    # * @author       wusicaijuan
    # * @date         2019.06.22
    # * @bried        控制某一直流电机停止转动
	# 					Control a DC motor to stop rotating
    # * @param[in]   index
    #                     1: M1
    #                     2: M2
    #                     3: M3
    #                     4: M4
    # * @retval       void
    def StopMotor(self, index):
        a = enMotors[index - 1]
        b = a + 1
        self.pca9685.set_pwm(a, 0, 0)
        self.pca9685.set_pwm(b, 0, 0)


    # * Function      MotorStopAll()
    # * @author       wusicaijuan
    # * @date         2019.06.22
    # * @bried        全部直流电机停止转动
	# 					All DC motors stop rotating
    # * @param[in]	  void
    # * @retval       void
    def MotorStopAll(self):
        self.stopMotor(1)
        self.stopMotor(2)
        self.stopMotor(3)
        self.stopMotor(4)
