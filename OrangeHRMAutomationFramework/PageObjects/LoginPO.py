from selenium.webdriver.common.by import By
from Utilities.SeleniumHelper import SeleniumHelpers

username_textbox = (By.NAME, "username")
password_textbox = (By.NAME, "password")
login_button = (By.XPATH, "//button[@type='submit']")


class LoginPO(SeleniumHelpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_login_form(self, value):
        self.enter_Text(username_textbox, value.get_userName())
        self.enter_Text(password_textbox, value.get_passWord())
        # self.click_On(login_button)




