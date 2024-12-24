from Raspi_MotorHAT import Raspi_MotorHAT
import atexit


I2C_ADDR = 0x60
MOTOR_CHANNEL_L = 3
MOTOR_CHANNEL_R = 4


class Robot:
    def __init__(self, motorhat_addr=I2C_ADDR):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.left_motor = self._mh.getMotor(MOTOR_CHANNEL_L)
        self.right_motor = self._mh.getMotor(MOTOR_CHANNEL_R)
        atexit.register(self.stop_motors)

    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
