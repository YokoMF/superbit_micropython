# Stepper Motor Shield/Wing Driver
# Based on Adafruit Motorshield library:
# https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library
# Author: Tony DiCola
from microbit import sleep, i2c
import PCA9685
import math
import motor

STP_CHA_L = 2047
STP_CHA_H = 4095

STP_CHB_L = 1
STP_CHB_H = 2047

STP_CHC_L = 1023
STP_CHC_H = 3071

STP_CHD_L = 3071
STP_CHD_H = 1023

enSteppers = (0x1, 0x2)

# blockId="T1B4" block="1/4"
T1B4 = 90,
# blockId="T1B2" block="1/2"
T1B2 = 180,
# blockId="T1B0" block="1"
T1B0 = 360,
# blockId="T2B0" block="2"
T2B0 = 720,
# blockId="T3B0" block="3"
T3B0 = 1080,
# blockId="T4B0" block="4"
T4B0 = 1440,
# blockId="T5B0" block="5"
T5B0 = 1800
enTurns = (T1B4, T1B2, T1B0, T2B0, T3B0, T4B0, T5B0)

m2 = motor.DCMotors(i2c)

class Steppers:
    def __init__(self, i2c, address=0x40, freq=50):
        self.pca9685 = PCA9685.PCA9685(i2c, address)
        self.pca9685.set_pwm_freq(freq)

    def setStepper(self, index, dir:bool):
        if index == enSteppers[index-1]:
            if dir:
                self.pca9685.set_pwm(11, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(9, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(10, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(8,STP_CHD_L, STP_CHD_H)
            else:
                self.pca9685.set_pwm(8, STP_CHA_L, STP_CHA_H)
                self.pca9685.set_pwm(10, STP_CHB_L, STP_CHB_H)
                self.pca9685.set_pwm(9, STP_CHC_L, STP_CHC_H)
                self.pca9685.set_pwm(11,STP_CHD_L, STP_CHD_H)
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
                self.pca9685.set_pwm(12,STP_CHD_L, STP_CHD_H)

    def StepperDegree(self, index, degree):
        # if degree > 0:
        self.setStepper(enSteppers[index-1], degree > 0)
        degree = abs(degree)
        pause(10240 * degree / 360)
        m2.MotorStopAll()

    def StepperTurn(self, index, turn):
        degree = enTurns[turn-1]
        self.StepperDegree(enSteppers[index-1], degree)
























# # Constants that specify the direction and style of steps.
# FORWARD = const(1)
# BACKWARD = const(2)
# SINGLE = const(1)
# DOUBLE = const(2)
# INTERLEAVE = const(3)
# MICROSTEP = const(4)

# # Not a const so users can change this global to 8 or 16 to change step size
# MICROSTEPS = 16

# # Microstepping curves (these are constants but need to be tuples/indexable):
# _MICROSTEPCURVE8 = (0, 50, 98, 142, 180, 212, 236, 250, 255)
# _MICROSTEPCURVE16 = (0, 25, 50, 74, 98, 120, 141, 162, 180, 197, 212, 225, 236, 244, 250, 253, 255)

# # Define PWM outputs for each of two available steppers.
# # Each tuple defines for a stepper: pwma, ain2, ain1, pwmb, bin2, bin1
# _STEPPERS = ((8, 9, 10, 13, 12, 11), (2, 3, 4, 7, 6, 5))


# class StepperMotor:
#     def __init__(self, pca, pwma, ain2, ain1, pwmb, bin2, bin1):
#         self.pca9685 = pca
#         self.pwma = pwma
#         self.ain2 = ain2
#         self.ain1 = ain1
#         self.pwmb = pwmb
#         self.bin2 = bin2
#         self.bin1 = bin1
#         self.currentstep = 0

#     def _pwm(self, pin, value):
#         if value > 4095:
#             self.pca9685.pwm(pin, 4096, 0)
#         else:
#             self.pca9685.pwm(pin, 0, value)

#     def _pin(self, pin, value):
#         if value:
#             self.pca9685.pwm(pin, 4096, 0)
#         else:
#             self.pca9685.pwm(pin, 0, 0)

#     def onestep(self, direction, style):
#         ocra = 255
#         ocrb = 255
#         # Adjust current steps based on the direction and type of step.
#         if style == SINGLE:
#             if (self.currentstep//(MICROSTEPS//2)) % 2:
#                 if direction == FORWARD:
#                     self.currentstep += MICROSTEPS//2
#                 else:
#                     self.currentstep -= MICROSTEPS//2
#             else:
#                 if direction == FORWARD:
#                     self.currentstep += MICROSTEPS
#                 else:
#                     self.currentstep -= MICROSTEPS
#         elif style == DOUBLE:
#             if not (self.currentstep//(MICROSTEPS//2)) % 2:
#                 if direction == FORWARD:
#                     self.currentstep += MICROSTEPS//2
#                 else:
#                     self.currentstep -= MICROSTEPS//2
#             else:
#                 if direction == FORWARD:
#                     self.currentstep += MICROSTEPS
#                 else:
#                     self.currentstep -= MICROSTEPS
#         elif style == INTERLEAVE:
#             if direction == FORWARD:
#                 self.currentstep += MICROSTEPS//2
#             else:
#                 self.currentstep -= MICROSTEPS//2
#         elif style == MICROSTEP:
#             if direction == FORWARD:
#                 self.currentstep += 1
#             else:
#                 self.currentstep -= 1
#             self.currentstep += MICROSTEPS*4
#             self.currentstep %= MICROSTEPS*4
#             ocra = 0
#             ocrb = 0
#             if MICROSTEPS == 8:
#                 curve = _MICROSTEPCURVE8
#             elif MICROSTEPS == 16:
#                 curve = _MICROSTEPCURVE16
#             else:
#                 raise RuntimeError('MICROSTEPS must be 8 or 16!')
#             if 0 <= self.currentstep < MICROSTEPS:
#                 ocra = curve[MICROSTEPS - self.currentstep]
#                 ocrb = curve[self.currentstep]
#             elif MICROSTEPS <= self.currentstep < MICROSTEPS*2:
#                 ocra = curve[self.currentstep - MICROSTEPS]
#                 ocrb = curve[MICROSTEPS*2 - self.currentstep]
#             elif MICROSTEPS*2 <= self.currentstep < MICROSTEPS*3:
#                 ocra = curve[MICROSTEPS*3 - self.currentstep]
#                 ocrb = curve[self.currentstep - MICROSTEPS*2]
#             elif MICROSTEPS*3 <= self.currentstep < MICROSTEPS*4:
#                 ocra = curve[self.currentstep - MICROSTEPS*3]
#                 ocrb = curve[MICROSTEPS*4 - self.currentstep]
#         self.currentstep += MICROSTEPS*4
#         self.currentstep %= MICROSTEPS*4
#         # Set PWM outputs.
#         self._pwm(self.pwma, ocra*16)
#         self._pwm(self.pwmb, ocrb*16)
#         latch_state = 0
#         # Determine which coils to energize:
#         if style == MICROSTEP:
#             if 0 <= self.currentstep < MICROSTEPS:
#                 latch_state |= 0x3
#             elif MICROSTEPS <= self.currentstep < MICROSTEPS*2:
#                 latch_state |= 0x6
#             elif MICROSTEPS*2 <= self.currentstep < MICROSTEPS*3:
#                 latch_state |= 0xC
#             elif MICROSTEPS*3 <= self.currentstep < MICROSTEPS*4:
#                 latch_state |= 0x9
#         else:
#             latch_step = self.currentstep//(MICROSTEPS//2)
#             if latch_step == 0:
#                 latch_state |= 0x1  # energize coil 1 only
#             elif latch_step == 1:
#                 latch_state |= 0x3  # energize coil 1+2
#             elif latch_step == 2:
#                 latch_state |= 0x2  # energize coil 2 only
#             elif latch_step == 3:
#                 latch_state |= 0x6  # energize coil 2+3
#             elif latch_step == 4:
#                 latch_state |= 0x4  # energize coil 3 only
#             elif latch_step == 5:
#                 latch_state |= 0xC  # energize coil 3+4
#             elif latch_step == 6:
#                 latch_state |= 0x8  # energize coil 4 only
#             elif latch_step == 7:
#                 latch_state |= 0x9  # energize coil 1+4
#         # Energize coils as appropriate:
#         if latch_state & 0x1:
#             self._pin(self.ain2, True)
#         else:
#             self._pin(self.ain2, False)
#         if latch_state & 0x2:
#             self._pin(self.bin1, True)
#         else:
#             self._pin(self.bin1, False)
#         if latch_state & 0x4:
#             self._pin(self.ain1, True)
#         else:
#             self._pin(self.ain1, False)
#         if latch_state & 0x8:
#             self._pin(self.bin2, True)
#         else:
#             self._pin(self.bin2, False)
#         return self.currentstep
