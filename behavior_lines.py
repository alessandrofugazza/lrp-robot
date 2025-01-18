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

def float_in_range(float_value, min_value, max_value):
    float_value = float(float_value)
    if float_value < min_value or float_value > max_value:
        raise argparse.ArgumentTypeError(f"Value {float_value} is out of range [{min_value}, {max_value}]")
    return float_value

parser = argparse.ArgumentParser(description='Select a test.')
parser.add_argument('--ls', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for left motor as a percentage.')
parser.add_argument('--rs', type=lambda x: int_in_range(x, MIN_SPEED, MAX_SPEED), required=True, help='Speed for right motor as a percentage.')
parser.add_argument('--tt', type=lambda x: float_in_range(x, 0.1, 60.0), required=True, help='Duration to run the motors in seconds (0.1-60.0).')

args = parser.parse_args()

r = robot.Robot()

r.set_left(args.ls)
r.set_right(args.rs)

sleep(args.tt)