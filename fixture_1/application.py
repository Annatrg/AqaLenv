from selenium import webdriver
from fixture_1.card import CardHelper
from fixture_1.session import SessionHelper

class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.card = CardHelper(self)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()
