from selenium import webdriver
from time import sleep


class jamb_bot:
    def __init__(self):
        URL = "https://portal.jamb.gov.ng/efacility./"
        PATH = "./chrome_driver/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(URL)
        self.UTME_registration_number = input(
            "enter your utme registration number: ")
        self.site_xpaths = {
            "email_input_field": "//*[@id=\"email\"]",
            "password_input_field": "//*[@id=\"password\"]",
            "login_button": "//*[@id=\"lnkLogin\"]",
            "admission_status_box": "//*[@id=\"ctl00\"]/div[8]/div/div/div[15]/a",
            "check_admission_status_button": "//*[@id=\"MainContent_btnSearch\"]",
            "utme_number_input_field": "//*[@id=\"MainContent_RegNumber\"]",
            "admission_status_info": "//*[@id=\"MainContent_pnlPopUp\"]/div/div/div/div/b"
        }

    def get_credentials(self):
        user_email = input("enter your username/email: ")
        user_password = input("enter your password: ")
        return (user_email, user_password)

    def login(self):
        user_email, user_password = jamb_bot.get_credentials(self)
        email_input_element = self.driver.find_element_by_xpath(
            self.site_xpaths["email_input_field"])
        password_input_element = self.driver.find_element_by_xpath(
            self.site_xpaths["password_input_field"])
        login_button_element = self.driver.find_element_by_xpath(
            self.site_xpaths["login_button"])
        email_input_element.send_keys(user_email)
        password_input_element.send_keys(user_password)
        login_button_element.click()

    def navigate_to_admission_status(self):
        admission_status = self.driver.find_element_by_xpath(
            self.site_xpaths["admission_status_box"])
        admission_status.click()

    def check_admission_status(self):
        utme_number_input_element = self.driver.find_element_by_xpath(
            self.site_xpaths["utme_number_input_field"])
        check_admission_status_button = self.driver.find_element_by_xpath(
            self.site_xpaths["check_admission_status_button"])
        utme_number_input_element.send_keys(self.UTME_registration_number)
        sleep(3)
        check_admission_status_button.click()
        sleep(3)
        admission_status_info = self.driver.find_element_by_xpath(
            self.site_xpaths["admission_status_info"])
        status = admission_status_info.text
        return status
