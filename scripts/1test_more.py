from appium import webdriver
from time import sleep
from base.base_driver import init_driver
from page.mobile_network_page import MobileNetworkPage
from page.more_page import MorePage
from page.page import Page
from page.setting_page import SettingPage


class TestMore:
    def setup(self):
        self.driver = init_driver()
        # self.setting_page = SettingPage(self.driver)
        # self.more_page = MorePage(self.driver)
        # self.mobile_network_page = MobileNetworkPage(self.driver)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_more_2g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_network_2G()

    def test_more_3g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_network_3G()