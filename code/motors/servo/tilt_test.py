from robot import Robot

the_robot = Robot()

while True:
    tilt_value = int(input("Enter the tilt value: "))
    the_robot.set_tilt(tilt_value)