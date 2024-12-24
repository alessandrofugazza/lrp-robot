from Raspi_MotorHAT import Raspi_MotorHAT
import atexit


I2C_ADDR = 0x60
MOTOR_CHANNEL_L = 3
MOTOR_CHANNEL_R = 4

MAX_SPEED = 255

class Robot:

    def __init__(self, motorhat_addr=I2C_ADDR):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.left_motor = self._mh.getMotor(MOTOR_CHANNEL_L)
        self.right_motor = self._mh.getMotor(MOTOR_CHANNEL_R)
        atexit.register(self.stop_motors)

    def convert_speed(self, speed):
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        output_speed = (abs(speed) * MAX_SPEED) // 100
        return mode, int(output_speed)

    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)
        
    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
