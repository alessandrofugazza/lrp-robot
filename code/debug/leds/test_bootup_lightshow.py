from time import sleep
from robot import Robot
from led_bootup_lightshow import show_bootup_lightshow

bot = Robot()

while True:
    print("on")
    show_bootup_lightshow(bot.leds, range(bot.leds.count))
    # bot.leds.show()
    # sleep(0.5)
    # print("off")
    # bot.leds.clear()
    # bot.leds.show()
    # sleep(0.5)
    