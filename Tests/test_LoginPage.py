import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
import time

from Tests.test_Base import BaseTestLogger


@pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTestLogger):
    def test_signup_link_visible(self):
       self.login =LoginPage(self.driver)
       flag=  self.login.is_SignUp_Link_exist()
       assert flag

    def test_login_Page_Title(self):
        self.login = LoginPage(self.driver)
        title = self.login.get_login_page_title(TestData.Login_Page_Title)
        assert title==TestData.Login_Page_Title

    @pytest.mark.slow
    def test_login_for_Invalid_Credential(self):
            log=self.getLogger()
            self.login = LoginPage(self.driver)
            self.login.do_login(TestData.Username,TestData.Wrong_credential)
            flag=self.login.validate_error_for_invalid_credential()
            log.info(flag)
            assert flag

