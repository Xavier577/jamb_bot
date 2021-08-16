from time import sleep
from jamb_bot import jamb_bot


def admission_status():
    print("this a bot that logs into jamb and checks your admission status for you")
    bot = jamb_bot()
    bot.login()
    sleep(3)
    bot.navigate_to_admission_status()
    sleep(3)
    return bot.check_admission_status()


result = admission_status()
status = f" \n status: \n {result}"
print(status)
