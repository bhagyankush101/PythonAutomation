import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import time
@pytest.mark.usefixtures("init_driver")
class Test_Performance():
    def test_Navigate_to_Performance_NavBar(self):
        # self.login = LoginPage(self.driver)
        # homePage = self.login.do_login(TestData.Username, TestData.Password)
        homePage = HomePage(self.driver)
        performance_page= homePage.click_On_Performance_NavBar()
        performance_page.select_KPI_option_from_config_dropdown()
        performance_page.select_all_KPI_option()
        assert performance_page.get_Delete_Selected_Option_is_Displayed()

