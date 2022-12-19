class CardHelper:

    def __init__(self, app):
        self.app = app

    def value_card_list(self):
        wd = self.app.wd
        value_card_list = []
        value_card_list += wd.find_elements_by_class_name("par-options__button")
        return value_card_list

    def choose_card_value(self, value_card):
        wd = self.app.wd
        value_card.click()

    def button_is_active(self, button):
        return True if button.get_attribute("class") == 'par-options__button par-options__button--active' else False

    def get_card_value_from_button(self, button):
        return button.text

    def get_card_value_from_input(self):
        wd = self.app.wd
        card_value_from_input = wd.find_element_by_id("range-value-input").get_attribute("value")
        return card_value_from_input

    def check_button_is_active(self, value_card):
        assert self.button_is_active(value_card)

    def check_card_value_from_button_and_card_value_from_input(self, value_card):
        assert self.get_card_value_from_button(value_card) == self.get_card_value_from_input()
