import hw26


def test_hw26_returning_products_maximum_allowable_price_as_no_products_in_list():
    incoming_products_list = []
    max_value = 100
    assert hw26.returning_products_maximum_allowable_price(incoming_products_list, max_value) == []


def test_hw26_returning_products_maximum_allowable_price_as_there_is_no_suitable_product():
    incoming_products_list = [{'product': 'bred', 'price': 25}, {'product': 'lemon', 'price': 50}]
    max_value = 5
    assert hw26.returning_products_maximum_allowable_price(incoming_products_list, max_value) == []


def test_hw26_returning_products_maximum_allowable_price_as_everything_fits():
    incoming_products_list = [{'product': 'bred', 'price': 25}, {'product': 'lemon', 'price': 50}]
    max_value = 100
    assert hw26.returning_products_maximum_allowable_price(incoming_products_list, max_value) == ['bred', 'lemon']


def test_hw26_returning_products_maximum_allowable_price_as_some_fit_and_some_dont():
    incoming_products_list = [{'product': 'bred', 'price': 25}, {'product': 'lemon', 'price': 50}]
    max_value = 30
    assert hw26.returning_products_maximum_allowable_price(incoming_products_list, max_value) == ['bred']


def test_hw26_receives_number_and_generates_a_tape_of_this_length():
    number = 5
    assert hw26.receives_number_and_generates_a_tape_of_this_length(number).endswith('danKo')
