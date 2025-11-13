import pytest

from model.cpf import Cpf


@pytest.fixture
def cpf_samples():
    """
    Provides sample CPF strings for testing different validation case.

    Returns:
        - dict: Dictionary containing valid and invalid CPF examples.
    """
    return {
        'valid': '303.176.740-30',
        'invalid_format': '303.176.740-3A',
        'short': '1234567',
        'long': '12345678900000',
        'repeated': '111.111.111-11',
        'invalid_check': '303.176.740-41'
    }


@pytest.mark.parametrize('input_cpf, expected', [
    ('111.111.111-11', '11111111111'),
    ('11111111111', '11111111111'),
])
def test_clean_removes_non_digits(input_cpf, expected):
    """
    Ensures that CPF.clean() removes non-digit characters while keeping digits intact.

    Parameters (via parametrize):
        - input_cpf (str): CPF string to be cleaned.
        - expected (str): Expected cleaned CPF contained only digits.
    """
    assert Cpf.clean(input_cpf) == expected


@pytest.mark.parametrize('cpf_key, expected', [
    ('valid', True),
    ('invalid_format', False),
    ('short', False),
    ('long', False),
    ('repeated', False),
    ('invalid_check', False),
])
def test_validate_various_cpfs(cpf_samples, cpf_key, expected):
    """
    Validates different CPF inputs using Cpf.validate().

    Parameters (via parametrize):
        - cpf_key (str): Key to select which CPF sample to validate.
        - expected (bool): Expected validation result.

    Fixture:
        - cpf_samples: Provides different CPF cases (valid and invalid).
    """
    cpf_value = cpf_samples[cpf_key]
    assert Cpf.validate(cpf_value) is expected


def test_calculate_check_digit_first_and_second():
    """
    Ensure that Cpf.__calculate_check_digit() correctly computes both check digits.
    """
    cpf_digits = "303176740"
    expected_first_digit = 3
    expected_second_digit = 0
    first_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=9, initial_weight=10)  # type: ignore
    second_digit = Cpf._Cpf__calculate_check_digit(cpf_digits + str(first_digit), length=10, initial_weight=11)  # type: ignore
    assert (first_digit, second_digit) == (expected_first_digit, expected_second_digit)


@pytest.mark.parametrize('digits, weight, expected', [
    ("303", 5, 24),
    ("", 5, 0)
])
def test_recursive_weighted_sum_calculation(digits, weight, expected):
    """
    Ensures that the private recursive method correctly calculates the weighted sum.

    Parameters (via parametrize):
        - digits (str): Sequence of numeric digits.
        - weight (int): Initial weight for calculation.
        - expected (int): Expected weighted sum result.
    """
    result = Cpf._Cpf__recursive_weighted_sum(digits, weight)  # type: ignore
    assert result == expected
