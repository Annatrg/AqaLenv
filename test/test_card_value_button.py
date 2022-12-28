import allure
from digift.page_objects.digift_page import DigiftPage


def test_card_value_button(app, load_config):
    digift_page = DigiftPage(app, load_config['baseUrl'])
    digift_page.basic_auth(load_config['login'], load_config['password'])
    for value_card in digift_page.value_card_list():
        with allure.step(f'Проверка клика по кнопке с номиналом {digift_page.get_card_value_from_button(value_card)}'):
            digift_page.choose_card_value(value_card)
        with allure.step(f'Проверка активности кнопки номиналом {digift_page.get_card_value_from_button(value_card)}'):
            digift_page.check_button_is_active(value_card)
        with allure.step(f'Сравнение значения кнопки с номиналом {digift_page.get_card_value_from_button(value_card)} '
                         f'со значением из поля ввода'):
            digift_page.check_card_value_from_button_and_card_value_from_input(value_card)
