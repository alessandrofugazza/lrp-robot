import ledshim
from time import sleep
import sys

class Leds:
    @property
    def count(self):
        return ledshim.width
    
    def set_one(self, led_number, color):
        ledshim.set_pixel(led_number, *color)

    def set_range(self, led_range, color):
        ledshim.set_multiple_pixels(led_range, color)

    def set_all(self, color):
        ledshim.set_all(*color)

    def clear(self): 
        ledshim.clear()

    def show(self): 
        ledshim.show()

    def boot_light_show(self):
        while True:
            for led_no in range(self.count):
                ledshim.set_pixel(led_no, 0, 255, 0)
                ledshim.show()
                sleep(0.1)
                ledshim.clear()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "boot_light_show":
        leds = Leds()
        leds.boot_light_show()