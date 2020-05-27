from appium import webdriver
from time import sleep

class TestDisplay:
    def setup(self):
        desired_caps = {}
        # 设备系统
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '5.1'
        # 设备名称
        desired_caps['deviceName'] = '192.168.126.101:5555'
        # 包名
        desired_caps['appPackage'] = 'com.android.settings'
        # 界面名
        desired_caps['appActivity'] = '.Settings'
        # 启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_display_search(self):
        self.driver.find_element_by_xpath("//*[@text='显示']").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()