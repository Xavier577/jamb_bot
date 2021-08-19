import platform
from selenium import webdriver


def driver():
    operating_system = platform.system()
    WINDOWS_PATH = "./chrome_driver/windows/chromedriver"
    LINUX_PATH = "./chrome_driver/linux/chromedriver"
    MAC_PATH = "./chrome_driver/mac/chromedriver"
    if operating_system == "Windows":
        return webdriver.Chrome(WINDOWS_PATH)
    if operating_system == "Linux":
        return webdriver.Chrome(LINUX_PATH)
    if operating_system == "Darwin":
        return webdriver.Chrome(MAC_PATH)
