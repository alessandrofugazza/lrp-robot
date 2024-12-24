import argparse
import robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep

MIN_SPEED = -100
MAX_SPEED = 100

def int_in_range(int_value, min_value, max_value):
    int_value = int(int_value)
    if int_value < min_value or int_value > max_value:
        raise argparse.ArgumentTypeError(f"Value {int_value} is out of range [{min_value}, {max_value}]")
    return int_value

parser = argparse.ArgumentParser(description='Select a test.')
parser.add_argument('--left_speed', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for left motor as a percentage.')
parser.add_argument('--right_speed', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for right motor as a percentage.')
parser.add_argument('--test_time', type=lambda x: int_in_range(x, 1, 60), required=True, help='Duration to run the motors in seconds (1-60).')

args = parser.parse_args()

r = robot.Robot()

r.set_left(args.left_speed)
r.set_right(args.right_speed)

sleep(args.test_time)