import hw27


def test_checking_validation_short_password():
    password = 'Aa1!'
    assert hw27.checking_validation_password(password) is False


def test_checking_validation_correct_password():
    password = 'aABb1234!@#'
    assert hw27.checking_validation_password(password) is True


def test_checking_validation_none_uppercase_password():
    password = 'ab1234!@#'
    assert hw27.checking_validation_password(password) is False


def test_checking_validation_none_lowercase_password():
    password = 'AB1234!@#'
    assert hw27.checking_validation_password(password) is False


def test_checking_validation_none_digit_password():
    password = 'abadadadada'
    assert hw27.checking_validation_password(password) is False


def test_checking_validation_none_password():
    password = ''
    assert hw27.checking_validation_password(password) is False


def test_checking_validation_space_in_password():
    password = 'aABb1234!@# '
    assert hw27.checking_validation_password(password) is False
