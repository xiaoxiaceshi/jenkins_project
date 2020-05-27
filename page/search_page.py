from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):
    search_edit_text = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    def input_search(self,content):
        self.input(self.search_edit_text,content)

    def click_back(self):
        self.click(self.back_button)