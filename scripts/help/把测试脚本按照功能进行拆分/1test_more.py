from appium import webdriver
from time import sleep

class TestMore:
    def setup(self):
        desired_caps = {}
        #设备系统
        desired_caps['platformName'] = 'Android'
        #设备系统版本
        desired_caps['platformVersion'] = '5.1'
        #设备名称
        desired_caps['deviceName'] = '192.168.126.101:5555'
        #包名
        desired_caps['appPackage'] = 'com.android.settings'
        #界面名
        desired_caps['appActivity'] = '.Settings'
        #启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_more_2g(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='2G']").click()

    def test_more_3g(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='3G']").click()