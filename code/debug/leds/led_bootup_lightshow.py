from time import sleep

def show_bootup_lightshow(leds, led_range):
    led_range = list(led_range)
    direction = 1
    index = 0

    while True:
        leds.set_one(led_range[index], (0, 255, 0))
        leds.show()
        sleep(0.01)
        leds.clear()

        index += direction
        if index == len(led_range) - 1 or index == 0:
            direction *= -1