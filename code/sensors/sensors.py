import argparse
import robot

def float_in_range(float_value, min_value, max_value):
    float_value = float(float_value)
    if float_value < min_value or float_value > max_value:
        raise argparse.ArgumentTypeError(f"Value {float_value} is out of range [{min_value}, {max_value}]")
    return float_value

parser = argparse.ArgumentParser(description='Optionally select a frequency.')

parser.add_argument('--f', type=lambda x: float_in_range(x, 0.1, 10.0), default=0.1, help='Frequency (0.1-10.0).')

args = parser.parse_args()

r = robot.Robot()

r.sensors_trig(args.f)