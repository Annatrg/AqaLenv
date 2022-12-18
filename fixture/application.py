from selenium import webdriver
from fixture.card import CardHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.card = CardHelper(self)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()
