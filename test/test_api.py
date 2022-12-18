

def test_api(config_task2):
    products = config_task2.get_results(search="Alcatel", sort_field="name")
    for product in products:
        assert product.name.count("Alcatel") > 0
    name = [x.name for x in products]
    assert name == sorted(name)
