import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import time

@pytest.mark.usefixtures("init_driver")
class Test_MyInfo():

    @pytest.mark.order(3)
    def test_validate_profile_icon(self):
        # self.login = LoginPage(self.driver)
        # homePage = self.login.do_login(TestData.Username, TestData.Password)
        homePage = HomePage(self.driver)
        myinfo = homePage.click_On_My_Info_NavBar()
        myinfo.click_on_profile_Icon()
        print(myinfo.get_profileICon_text())
        assert myinfo.get_profileICon_text() == TestData.profile_Icon_detail

    @pytest.mark.order(2)
    def test_Tax_Exemptions(self):
        # self.login = LoginPage(self.driver)
        # homePage = self.login.do_login(TestData.Username, TestData.Password)
        homePage = HomePage(self.driver)
        myinfo = homePage.click_On_My_Info_NavBar()
        myinfo.click_on_Tax_Exemptions()
        flag = myinfo.element_is_disabled()
        assert flag

    @pytest.mark.order(1)
    def test_validate_to_upload_file(self):
        # self.login = LoginPage(self.driver)
        # homePage = self.login.do_login(TestData.Username, TestData.Password)
        homePage = HomePage(self.driver)
        myinfo = homePage.click_On_My_Info_NavBar()
        myinfo.click_on_Add_button_for_upload_file()
        myinfo.upload_File()
        myinfo.click_on_save_button()
        flag = myinfo.validate_errormessage()
        assert flag
