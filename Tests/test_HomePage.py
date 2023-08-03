import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import time

from Tests.test_Base import BaseTestLogger


@pytest.mark.usefixtures("init_driver")
class Test_Home(BaseTestLogger):

    def test_home_Page_title(self):

        homePage = HomePage(self.driver)
        title = homePage.get_Home_Page_Title(TestData.Login_Page_Title)
        assert title == TestData.Login_Page_Title

    @pytest.mark.slow
    def test_home_Page_Header(self):

        homePage = HomePage(self.driver)
        homePage.click_on_DashBoard_Navbar()
        header=homePage.get_Header_Page()

        assert header == TestData.Home_Page_Header

    def test_help_icon_exist(self):

        homePage=HomePage(self.driver)
        #homepage
        ele=homePage.mouse_over_element()
        print(ele)
        print("Hello")
        assert homePage.is_Help_IconExist()

