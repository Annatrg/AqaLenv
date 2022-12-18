# from model.card import Card

def test_card_value_button(app):
    for value_card in app.card.value_card_list():
        app.card.choose_card_value(value_card)
        assert app.card.get_card_value_from_button(value_card) == app.card.get_card_value_from_input()
