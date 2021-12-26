from time import sleep
from jamb_bot import JAMB_BOT


def admission_status():
    print("this a bot that logs into jamb and checks your admission status for you")
    bot = JAMB_BOT()
    bot.login()
    sleep(3)
    bot.navigate_to_admission_status()
    sleep(4)
    return bot.check_admission_status()


def print_outcome():
    result = admission_status()
    status = f" \n status: \n {result}"
    print(status)
