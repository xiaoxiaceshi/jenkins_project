from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MorePage(BaseAction):
    mobile_network_button = By.XPATH,"//*[@text='移动网络']"

    def click_mobile_network(self):
        self.click(self.mobile_network_button)
