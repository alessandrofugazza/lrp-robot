from Raspi_MotorHAT import Raspi_MotorHAT
import time
import atexit

mh = Raspi_MotorHAT(addr=0x60)
lm = mh.getMotor(3)
rm = mh.getMotor(4)

def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

lm.setSpeed(150)
rm.setSpeed(150)
lm.run(Raspi_MotorHAT.FORWARD)
rm.run(Raspi_MotorHAT.FORWARD)
time.sleep(2)
