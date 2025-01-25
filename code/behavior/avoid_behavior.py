from robot import Robot
from time import sleep

SPEED = 80
# AVOIDANCE_DISTANCE = 300

class ObstacleAvoidingBehavior:
    """Simple obstacle avoiding"""
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = SPEED
        # self.led_half = int(self.robot.leds.leds_count/2)

    # def get_motor_speed(self, distance):
    #     """This method chooses a speed for a motor based on the distance from a sensor"""
    #     if distance < AVOIDANCE_DISTANCE:
    #         return -self.speed
    #     else:
    #         return self.speed

    def get_speeds(self, nearest_distance):
        if nearest_distance >= 1000: 
            nearest_speed = self.speed 
            furthest_speed = self.speed
            delay = 100
        elif nearest_distance > 500:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.8
            delay = 100
        elif nearest_distance > 200:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.6
            delay = 100
        elif nearest_distance > 100:
            nearest_speed = -self.speed * 0.4
            furthest_speed = -self.speed
            delay = 100
        else:
            # collision
            nearest_speed = -self.speed
            furthest_speed = -self.speed
            delay = 250
        return nearest_speed, furthest_speed, delay
    
    def display_state(self, left_distance, right_distance, nearest_speed, furthest_speed, delay):
        if left_distance == 1000.0:
            p_left_distance = "INF"
        else:
            p_left_distance = str(round(left_distance, 1)) + " mm"
        if right_distance == 1000.0:
            p_right_distance = "INF"
        else:
            p_right_distance = str(round(right_distance, 1)) + " mm"
        print(f'DISTANCES:\t\tLEFT\t{p_left_distance}\tRGTH\t{p_right_distance}\nSPEEDS:\t\tNRST\t{nearest_speed}\tFRST\t{furthest_speed}\nDLAY:\t\t{delay}\n\n')
        
    def run(self):
        # self.robot.set_pan(0)
        # self.robot.set_tilt(0)

        while True: 
            # turn into mm
            left_distance = self.robot.left_distance_sensor.distance * 1000
            right_distance = self.robot.right_distance_sensor.distance * 1000

            nearest_speed, furthest_speed, delay = self.get_speeds(min(left_distance, right_distance))
            self.display_state(left_distance, right_distance, nearest_speed, furthest_speed, delay)
            
            if left_distance < right_distance:
                self.robot.set_left(nearest_speed)
                self.robot.set_right(furthest_speed)
            else:
                self.robot.set_right(nearest_speed)
                self.robot.set_left(furthest_speed)
                # Wait a little 
                sleep(delay * 0.001)
    
bot = Robot()
behavior = ObstacleAvoidingBehavior(bot)
behavior.run()