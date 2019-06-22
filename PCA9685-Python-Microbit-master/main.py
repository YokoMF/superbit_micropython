# 在这里写上你的代码 :-)
from microbit import sleep, i2c
import PCA9685
import servo
import stepper

# Initialise the PCA9685 using the default address (0x40).
# pwm = PCA9685.PCA9685(i2c)

# Configure min and max servo pulse lengths (will need to adjust for different servos)
# servo_min = 150  # Min pulse length out of 4096
# servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
# pwm.set_pwm_freq(60)

# print('Moving servo on channel 0, press Ctrl-C to quit...')

# # Move servo on channel O between extremes.
# pwm.set_pwm(3, 0, servo_min)
# sleep(1000)
# pwm.set_pwm(3, 0, servo_max)
# sleep(1000)

# 驱动舵机
# Use servo helper class to move channel 0 by degrees
s0 = servo.Servos(i2c)
# s0.position(4, 0)
# s0.position(5, 0)
# sleep(1000)
# s0.position(4, 90)
# s0.position(5, 90)
# sleep(1000)
# s0.release(0)


# 驱动电机
# m1 = motor.DCMotors(i2c)
# m1.MotorRun(1, 255)
# sleep(1000)

# 驱动步进电机
step1 = stepper.Steppers(i2c)
step1.StepperDegree(1, -90)
sleep(1000)
step1.StepperTurn(1, 3)

# pwm.set_pwm(11, 0, 4095)
# pwm.set_pwm(10, 0, 0)
# pwm.set_pwm(8, 0, 4095)
# pwm.set_pwm(9, 0, 0)