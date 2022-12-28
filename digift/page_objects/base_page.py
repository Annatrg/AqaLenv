from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, wd, baseUrl):
        self.wd = wd
        self.baseUrl = baseUrl

    def basic_auth(self, login, password):
        self.wd.get(f"http://{login}:{password}@{self.baseUrl}")

    def find_element(self, locator, time=3):
        return WebDriverWait(self.wd, time).until(ec.presence_of_element_located(locator),
                                                  message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=3):
        return WebDriverWait(self.wd, time).until(ec.presence_of_all_elements_located(locator),
                                                  message=f"Can't find elements by locator {locator}")
