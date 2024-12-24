import argparse
from Raspi_MotorHAT import Raspi_MotorHAT
import time
import atexit

I2C_ADDR = 0x60
MOTOR_CHANNEL_L = 3
MOTOR_CHANNEL_R = 4

MIN_SPEED = -255
MAX_SPEED = 255

def int_in_range(int_value, min_value, max_value):
    int_value = int(int_value)
    if int_value < min_value or int_value > max_value:
        raise argparse.ArgumentTypeError(f"Value {int_value} is out of range [{min_value}, {max_value}]")
    return int_value

parser = argparse.ArgumentParser(description='Select a test.')
parser.add_argument('--mcls', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for left motor.')
parser.add_argument('--mcrs', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for right motor.')
parser.add_argument('--test_time', type=lambda x: int_in_range(x, 1, 60), required=True, help='Duration to run the motors in seconds (1-60).')

args = parser.parse_args()


mh = Raspi_MotorHAT(addr=I2C_ADDR)
lm = mh.getMotor(MOTOR_CHANNEL_L)
rm = mh.getMotor(MOTOR_CHANNEL_R)

def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

left_motor_abs_speed = abs(args.mcls)
right_motor_abs_speed = abs(args.mcrs)

if args.mcls >= 0:
    lm.run(Raspi_MotorHAT.FORWARD)
else:
    lm.run(Raspi_MotorHAT.BACKWARD)

if args.mcrs >= 0:
    rm.run(Raspi_MotorHAT.FORWARD)
else:
    rm.run(Raspi_MotorHAT.BACKWARD)

lm.setSpeed(left_motor_abs_speed)
rm.setSpeed(right_motor_abs_speed)

# lm.run(Raspi_MotorHAT.FORWARD)
# rm.run(Raspi_MotorHAT.FORWARD)
time.sleep(args.test_time)
