from selenium.webdriver.common.by import By
from .BasePage import BasePage
from ..Config.config import TestData

class HomePage(BasePage):
    HEADER = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6")
    ACCOUNT_ICON = (By.CLASS_NAME, "oxd-userdropdown-tab")
    ACCOUNT_DETAILS = (By.CLASS_NAME, "oxd-dropdown-menu")
    ACCOUNT_NAME = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]//li[1]')

    def __init__(self, driver):
        super().__init__(driver)
    
    def get_home_page_title(self, title):
        return self.get_title(title)
    
    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)
    
    def is_account_details_visible(self):
        self.do_click(self.ACCOUNT_ICON)
        return self.is_visible(self.ACCOUNT_DETAILS)
    
    def get_account_name(self):
        return self.get_element_text(self.ACCOUNT_NAME)
