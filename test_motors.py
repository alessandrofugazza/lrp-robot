from Raspi_MotorHAT import Raspi_MotorHAT
import time
import atexit

I2C_ADDR = 0x60
MOTOR_CHANNEL_L = 3
MOTOR_CHANNEL_R = 4
TEST_SPEED = 150
TEST_TIME = 2


mh = Raspi_MotorHAT(addr=I2C_ADDR)
lm = mh.getMotor(MOTOR_CHANNEL_L)
rm = mh.getMotor(MOTOR_CHANNEL_R)

def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

lm.setSpeed(TEST_SPEED)
rm.setSpeed(TEST_SPEED)
lm.run(Raspi_MotorHAT.FORWARD)
rm.run(Raspi_MotorHAT.FORWARD)
time.sleep(TEST_TIME)
