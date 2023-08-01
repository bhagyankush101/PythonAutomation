from Locators.Home_Page_Locators import HomePageLocators
from Pages.MyInfoPage import MyInfoPage
from Pages.PerformancePage import PerformancePage
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class HomePage(BasePage):



    def __init__(self, driver):
        super().__int__(driver)

    def get_Home_Page_Title(self,title):
        return self.get_title(title)
    def is_Help_IconExist(self):
        return self.is_visible((By.XPATH,HomePageLocators.HELP_ICON))
    def get_Header_Page(self):
        if self.is_visible(HomePageLocators.HEADER):
            return self.get_element_text(HomePageLocators.HEADER)
    def click_On_Performance_NavBar(self):
        self.do_click(HomePageLocators.PERFORMANCE_NAVBAR)
        return PerformancePage(self.driver)

    def click_On_Admin_NavBar(self):
            self.do_click(HomePageLocators.Admin_NAVBAR)
            return PerformancePage(self.driver)

    def click_On_My_Info_NavBar(self):
        self.do_click(HomePageLocators.My_info)
        return MyInfoPage(self.driver)

    def mouse_over_element(self):
        self.Mouse_Over_Element(HomePageLocators.HELP_ICON)
        return self.get_Attribute_title(HomePageLocators.HELP_ICON)

    def scroll_down(self):
        try:
         self.scroll_down_towards_element(HomePageLocators.ORANGE_HRM)
        except Exception as e:
         print(e)
    def click_on_DashBoard_Navbar(self):
        self.do_click(HomePageLocators.DASHBOARD_NAVBAR)
