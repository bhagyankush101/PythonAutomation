import time

from Locators.My_Info_Page_Locators import MyInfoLocators
from Locators.Performance_Page_Locators import PerformancePageLocators
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class MyInfoPage(BasePage):


    def __init__(self, driver):
        super().__int__(driver)

    def click_on_profile_Icon(self):
        self.do_click(MyInfoLocators.Profile_Picture)

    def get_profileICon_text(self):
       text_data= self.get_element_text1(MyInfoLocators.Picture_upload_details)
       return text_data
    def click_on_Tax_Exemptions(self):
        self.do_click(MyInfoLocators.Tax_Exemptions)

    def element_is_disabled(self):
       return self.is_disabled(MyInfoLocators.state)

    def click_on_Add_button_for_upload_file(self):
        self.driver.execute_script("window.scrollTo(0,1000)")
        self.do_click(MyInfoLocators.Add_button_Upload_File)
        self.driver.execute_script("window.scrollTo(0,1500)")

    def upload_File(self):
        self.do_send_Keys1(MyInfoLocators.upload_file,TestData.Filepath)

    def click_on_save_button(self):
        self.do_click(MyInfoLocators.save_button)
    def validate_errormessage(self):
      return  self.is_visible((By.CSS_SELECTOR,MyInfoLocators.ErrorMessage))
