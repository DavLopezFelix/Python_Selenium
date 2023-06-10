import pytest
from ..Config.config import TestData
from ..Tests.test_base import BaseTest
from ..Pages.LoginPage import LoginPage

class Test_Login(BaseTest):

    def test_singup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_visible()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
    
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

