import hw27
import pytest

test_cases_password = [
    ('aABb1234!@#', True),
    ('Aa1!', False),
    ('ab1234!@#', False),
    ('AB1234!@#', False),
    ('abcde', False),
    ('', False),
    ('aABb1234!@# ', False)
]


@pytest.mark.parametrize('password, expected', test_cases_password)
def test_checking_validation_password(password, expected):
    assert hw27.checking_validation_password(password) == expected
