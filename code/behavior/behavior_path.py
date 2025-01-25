import robot
from time import sleep

DEFAULT_SPEED = 50
TURN_SPEED = 20
DEFAULT_DURATION = 2.0

bot = robot.Robot()

def straight(bot = bot, seconds = DEFAULT_DURATION):
    bot.set_left(DEFAULT_SPEED)
    bot.set_right(DEFAULT_SPEED)
    sleep(seconds)

def turn_left(bot = bot, seconds = DEFAULT_DURATION):
    bot.set_left(TURN_SPEED)
    bot.set_right(DEFAULT_SPEED)
    sleep(seconds)

def turn_right(bot = bot, seconds = DEFAULT_DURATION):
    bot.set_left(DEFAULT_SPEED)
    bot.set_right(TURN_SPEED)
    sleep(seconds)

def spin_left(bot = bot, seconds = DEFAULT_DURATION):
    bot.set_left(-DEFAULT_SPEED)
    bot.set_right(DEFAULT_SPEED)
    sleep(seconds)

def stop(bot = bot, seconds = DEFAULT_DURATION):
    bot.set_left(0)
    bot.set_right(0)
    sleep(seconds)

# straight()
# stop()
# spin_left()
# stop()
# straight()
# turn_left(bot, 1)
# straight(bot, 1)
# turn_left(bot, 1)
# straight(bot, 1)
# spin_left(bot, 1)