from appium import webdriver
from time import  sleep
import pytest

class TestContact:

    def setup(self):
        desired_caps = {}
        #设备系统
        desired_caps['platformName'] = 'Android'
        #设备系统版本
        desired_caps['platformVersion'] = '5.1'
        #设备名称
        desired_caps['deviceName'] = '192.168.126.101:5555'
        #包名
        desired_caps['appPackage'] = 'com.android.contacts'
        #界面名
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        #启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 单个参数化
    @pytest.mark.parametrize("name",["zhangsan","lisi","wangwu"])
    def test_add_contact(self,name):
        # 点击添加联系人
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        # 点击本地保存
        self.driver.find_element_by_xpath("//*[@text='本地保存']").click()
        # 点击联系人姓名
        self.driver.find_element_by_xpath("//*[@text='姓名']").send_keys(name)

    # 多个参数化
    @pytest.mark.parametrize(("name","phone"), [("zhangsan","18311111111"), ("lisi","18322222222")])
    def test_add_contact(self, name,phone):
        # 点击添加联系人
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        # 点击本地保存
        self.driver.find_element_by_xpath("//*[@text='本地保存']").click()
        # 输入联系人姓名
        self.driver.find_element_by_xpath("//*[@text='姓名']").send_keys(name)
        # 输入联系人手机号
        self.driver.find_element_by_xpath("//*[@text='电话']").send_keys(phone)