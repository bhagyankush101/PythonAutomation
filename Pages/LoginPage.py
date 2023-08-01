import time

from Config.config import TestData
from selenium.webdriver.common.by import By
from Locators.Login_Locators import LoginLocators
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):


    def __init__(self,driver):
        super().__int__(driver)


    def get_login_page_title(self,title):
        return self.get_title(title)

    def is_SignUp_Link_exist(self):
        return self.is_visible(LoginLocators.SignUP_Link)

    def do_login(self,username,password):
            self.do_send_keys(LoginLocators.Email, username)
            self.do_send_keys(LoginLocators.Password, password)
            self.do_click(LoginLocators.Login_Button)
            time.sleep(2)
            return HomePage(self.driver)
    def validate_error_for_invalid_credential(self):
        return self.is_visible((By.XPATH,LoginLocators.Invalid_Credential))