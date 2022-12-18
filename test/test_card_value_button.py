import allure
from fixture.card import CardHelper


def test_card_value_button(app):
    for value_card in app.card.value_card_list():
        with allure.step(f'Проверка клика по кнопке с номиналом {app.card.get_card_value_from_button(value_card)}'):
            app.card.choose_card_value(value_card)
        with allure.step(f'Проверка активности кнопки с номиналом {app.card.get_card_value_from_button(value_card)}'):
            app.card.check_button_is_active(value_card)
        with allure.step(f'Сравнение значения из кнопки с номиналом {app.card.get_card_value_from_button(value_card)} '
                         f'со значением из поля ввода'):
            app.card.check_card_value_from_button_and_card_value_from_input(value_card)
