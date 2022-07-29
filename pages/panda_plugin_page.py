from pages.base_page import BasePage
from locators.panda_plugin_page_loc import PandaPluginPageLoc


class PandaPluginPage(BasePage):

    def validate_panda_title(self):
        panda_title_text = self.chrome.find_element(*PandaPluginPageLoc.shinning_panda_title_loc).text
        assert panda_title_text == 'ShiningPanda', 'Title is not ShiningPanda'
