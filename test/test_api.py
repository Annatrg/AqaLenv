def test_api(config_task2):
    products = config_task2.get_results(search="Alcatel", sort_field="name")
    for product in products:
        assert product.name.count("Alcatel") > 0
    product = [product.name for product in products]
    assert product == sorted(product)
