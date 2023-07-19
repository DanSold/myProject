import hw30


def test_generate_random_number():
    assert 1000 > hw30.generate_random_number() > 0
