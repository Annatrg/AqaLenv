def test_api(app2):
    products = app2.get_results(search="Alcatel", sort_field="name")
    for product in products:
        assert product.name.count("Alcatel") > 0
    product = [product.name for product in products]
    assert product == sorted(product)
