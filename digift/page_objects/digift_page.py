from selenium.webdriver.common.by import By
from digift.page_objects.base_page import BasePage


class DigiftSearchLocators:

    NOMINAL_BUTTONS = (By.CLASS_NAME, "par-options__button")
    ACTIVE_NOMINAL_BUTTONS = (By.CLASS_NAME, "par-options__button par-options__button--active")
    NOMINAL_VALUE = (By.ID, "range-value-input")


class DigiftPage(BasePage):

# Список номиналов карт
    def value_card_list(self):
        return self.find_elements(DigiftSearchLocators.NOMINAL_BUTTONS)

# Выбрать номинал карты
    def choose_card_value(self, value_card):
        value_card.click()

# Активна\неактивна кнопка
    def button_is_active(self, button):
        return True if button.get_attribute("class") == 'par-options__button par-options__button--active' else False

# Получение номинала активной карты
    def get_card_value_from_button(self, button):
        return button.text

# получение номинала карты из поля ввода
    def get_card_value_from_input(self):
        return self.find_element(DigiftSearchLocators.NOMINAL_VALUE).get_attribute("value")

# Проверка на активность кнопки
    def check_button_is_active(self, value_card):
        assert self.button_is_active(value_card)

# Проверка по сравнению значения из активной кнопки и поля ввода
    def check_card_value_from_button_and_card_value_from_input(self, value_card):
        assert self.get_card_value_from_button(value_card) == self.get_card_value_from_input()
