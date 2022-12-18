
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

    def get_card_value_from_button(self, button):
        return button.text

    def get_card_value_from_input(self):
        wd = self.app.wd
        card_value_from_input = wd.find_element_by_id("range-value-input").get_attribute("value")
        return card_value_from_input
