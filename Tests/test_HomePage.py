import pytest
from ..Pages.LoginPage import LoginPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest
from ..Pages.HomePage import HomePage

class Test_HomePage(BaseTest):

    def test_header_value(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        header = self.homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER
    
    def test_homePage_title(self):
        #self.loginPage = LoginPage(self.driver)
        #self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITTLE)
        assert title == TestData.HOME_PAGE_TITTLE

    def test_account_details_visible(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_account_details_visible()
        assert flag

    def test_account_email(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        name = self.homePage.get_account_name()
        assert name == TestData.NAME_ACCOUNT