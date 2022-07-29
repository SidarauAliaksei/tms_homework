import allure
import pytest
from selenium import webdriver
from pages.panda_plugin_page import PandaPluginPage


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('chromedriver.exe')
    browser.implicitly_wait(5)


@allure.story('Open ShiningPanda Plugin Page')
def test_guest_can_open_panda_plugin_page(open_browser):
    link = "https://plugins.jenkins.io/shiningpanda/"
    panda_plugin_page = PandaPluginPage(browser, link)

    try:
        panda_plugin_page.open()
        panda_plugin_page.validate_panda_title()
    finally:
        browser.quit()
