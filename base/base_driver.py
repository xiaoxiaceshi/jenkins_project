from appium import webdriver

def init_driver():
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
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)