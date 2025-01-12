import time
from gpiozero import DistanceSensor
# from gpiozero.pins.pigpio import PiGPIOFactory

print("Prepare GPIO Pins v2")
# sensor_l = DistanceSensor(echo=17, trigger=27, pin_factory=PiGPIOFactory())
# sensor_r = DistanceSensor(echo=5, trigger=6, pin_factory=PiGPIOFactory())
sensor_l = DistanceSensor(echo=17, trigger=27, queue_len=2)
sensor_r = DistanceSensor(echo=5, trigger=6, queue_len=2)

while True:
    # print("Left: {l}, Right: {r}".format( l=sensor_l.distance * 100, r=sensor_r.distance * 100))
    print("Right: {r}".format(r=sensor_r.distance * 100))
    time.sleep(0.1)
