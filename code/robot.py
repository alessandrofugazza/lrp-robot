import os
import time
from Raspi_MotorHAT import Raspi_MotorHAT
from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
import code.debug.leds.leds_led_shim as leds_led_shim

import atexit

# if os.system("pgrep pigpiod > /dev/null") != 0:
#     os.system("sudo pigpiod")
#     time.sleep(1) # todo check this timer

# if os.system("pgrep -f leds_led_shim.py > /dev/null") != 0:
#     os.system("python3 home/shell/leds_led_shim.py boot_light_show &")
#     time.sleep(1)


I2C_ADDR = 0x60

# should i move these?
MOTOR_CHANNEL_L, MOTOR_CHANNEL_R = 3, 4
LEFT_SENSOR_ECHO, LEFT_SENSOR_TRIGGER = 17, 27
RIGHT_SENSOR_ECHO, RIGHT_SENSOR_TRIGGER = 5, 6

MAX_SPEED = 255

class Robot:

    def __init__(self, motorhat_addr=I2C_ADDR):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.left_motor = self._mh.getMotor(MOTOR_CHANNEL_L)
        self.right_motor = self._mh.getMotor(MOTOR_CHANNEL_R)
        # Setup The Distance Sensors
        # consider starting pigpiod on boot
        pin_factory = PiGPIOFactory()
        self.left_distance_sensor = DistanceSensor(echo=LEFT_SENSOR_ECHO, trigger=LEFT_SENSOR_TRIGGER, pin_factory=pin_factory)
        self.right_distance_sensor = DistanceSensor(echo=RIGHT_SENSOR_ECHO, trigger=RIGHT_SENSOR_TRIGGER, pin_factory=pin_factory)
        self.leds = leds_led_shim.Leds()
        atexit.register(self.stop_all)

    def stop_all(self): 
        self.stop_motors() 
        self.leds.clear() 
        self.leds.show()

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

    def sensors_trig(self, frequency):
        while(True):
            ld, rd = round(self.sensor_l.distance * 1000, 1), round(self.sensor_r.distance * 1000, 1)
            # meh
            if ld == 1000.0:
                ld = "INF"
            else:
                ld = str(ld) + " mm"
            if rd == 1000.0:
                rd = "INF"
            else:
                rd = str(rd) + " mm"
            print(f'LEFT {ld}\tRIGHT {rd}')
            time.sleep(frequency)

    
