from robot import Robot
from time import sleep

SPEED = 50
AVOIDANCE_DISTANCE = 300

class ObstacleAvoidingBehavior:
    """Simple obstacle avoiding"""
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = SPEED

    def get_motor_speed(self, distance):
        """This method chooses a speed for a motor based on the distance from a sensor"""
        if distance < AVOIDANCE_DISTANCE:
            return -self.speed
        else:
            return self.speed
        
    def run(self):
        # self.robot.set_pan(0)
        # self.robot.set_tilt(0)

        while True: 
            left_distance = round(self.robot.left_distance_sensor.distance * 1000, 1)
            right_distance = round(self.robot.right_distance_sensor.distance * 1000, 1)
            if left_distance == 1000.0:
                p_left_distance = "INF"
            else:
                p_left_distance = str(left_distance) + " mm"
            if right_distance == 1000.0:
                p_right_distance = "INF"
            else:
                p_right_distance = str(right_distance) + " mm"
            print(f'LEFT {p_left_distance}\tRIGHT {p_right_distance}')
            left_speed = self.get_motor_speed(right_distance)
            self.robot.set_left(left_speed)
            right_speed = self.get_motor_speed(left_distance)
            self.robot.set_right(right_speed)
            # Wait a little 
            sleep(0.05)
    
bot = Robot()
behavior = ObstacleAvoidingBehavior(bot)
behavior.run()