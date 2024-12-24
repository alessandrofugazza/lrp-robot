from Raspi_MotorHAT import Raspi_MotorHAT
import atexit


I2C_ADDR = 0x60
MOTOR_CHANNEL_L = 3
MOTOR_CHANNEL_R = 4

# MIN_SPEED = -255
MAX_SPEED = 255

class Robot:
    def __init__(self, motorhat_addr=I2C_ADDR):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.left_motor = self._mh.getMotor(MOTOR_CHANNEL_L)
        self.right_motor = self._mh.getMotor(MOTOR_CHANNEL_R)
        atexit.register(self.stop_motors)
    def convert_speed(self, left_speed, right_speed): # should all this logic be here or in behavior_line.py?
        if left_speed >= 0:
            self.left_motor.run(Raspi_MotorHAT.FORWARD)
        else:
            self.left_motor.run(Raspi_MotorHAT.BACKWARD)
        self.left_motor.setSpeed((abs(left_speed) * MAX_SPEED) // 100)
        if right_speed >= 0:
            self.right_motor.run(Raspi_MotorHAT.FORWARD)
        else:
            self.right_motor.run(Raspi_MotorHAT.BACKWARD)
        self.right_motor.setSpeed((abs(left_speed) * MAX_SPEED) // 100)
    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
