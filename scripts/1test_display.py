from appium import webdriver
from time import sleep
from base.base_driver import init_driver
from page.display_page import DisplayPage
from page.page import Page
from page.search_page import SearchPage
from page.setting_page import SettingPage


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        # self.setting_page =  SettingPage(self.driver)
        # self.display_page = DisplayPage(self.driver)
        # self.search_page = SearchPage(self.driver)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_display_search(self):
        self.page.setting.click_display()
        self.page.display.click_search()
        self.page.search.input_search("hello")
        self.page.search.click_back()
