from Locators.Performance_Page_Locators import PerformancePageLocators
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class PerformancePage(BasePage):


    def __init__(self, driver):
        super().__int__(driver)

    def get_Home_Page_Title(self,title):
        return self.get_title(title)
    def is_User_Mgt_Exist(self):
        return self.is_visible(PerformancePageLocators.User_Mgt)
    def get_Header_Page(self):
        if self.is_visible(PerformancePageLocators.HEADER):
            return self.get_element_text(PerformancePageLocators.HEADER)

    def select_User_Mgt(self):
        self.do_click(PerformancePageLocators.Configure)
    def performance_tab_visible(self):
        self.is_visible(PerformancePageLocators.Configure)


    def select_KPI_option_from_config_dropdown(self):
      self.do_click(PerformancePageLocators.configure_tab)
      self.do_click(PerformancePageLocators.KPIs)

    def select_all_KPI_option(self):
        self.driver.execute_script("window.scrollTo(0,200)")
        self.do_click1(PerformancePageLocators.select_all_Key_PerformanceIndicator)

    def get_Delete_Selected_Option_is_Displayed(self):
        return self.is_visible(PerformancePageLocators.Delete_Selected)