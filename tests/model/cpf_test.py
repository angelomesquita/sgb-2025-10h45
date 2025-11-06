from model.cpf import Cpf


def test_clean_removes_non_digits():
    """Ensure non-digits characters are removed from CPF."""
    cpf = "111.111.111-11"
    cleaned = Cpf.clean(cpf)
    assert cleaned == '11111111111'


def test_clean_keeps_only_digits():
    """Ensure numbers remain unchanged after cleaning."""
    cpf = "11111111111"
    cleaned = Cpf.clean(cpf)
    assert cleaned == '11111111111'


def test_validate_return_true_for_valid_cpf():
    """Ensure valid CPF return True"""
    valid_cpf = "303.176.740-30"
    assert Cpf.validate(valid_cpf) is True


def test_validate_returns_false_for_invalid_format():
    """Ensure invalid CPF format return False"""
    invalid_cpf = "303.176.740-3A"
    assert Cpf.validate(invalid_cpf) is False


def test_validate_return_false_for_wrong_length():
    """Ensure CPF with incorrect length returns False"""
    short_cpf = "1234567"
    long_cpf = "12345678900000"
    assert not Cpf.validate(short_cpf)
    assert not Cpf.validate(long_cpf)


def test_validate_return_false_for_repeated_digits():
    """Ensure CPF with all identical digits returns False."""
    repeated_cpf = "111.111.111-11"
    assert Cpf.validate(repeated_cpf) is False


def test_validate_returns_false_for_invalid_check_digits():
    """Ensure CPF with wrong check digits returns False."""
    invalid_cpf = "303.176.740-41"
    assert Cpf.validate(invalid_cpf) is False


def test_calculate_check_digit_first_and_second():
    """Ensure check digit calculation returns expected digits."""
    cpf_digits = "303176740"
    expected_first_digit = 3
    expected_second_digit = 0
    first_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=9, initial_weight=10)  # type: ignore
    second_digit = Cpf._Cpf__calculate_check_digit(cpf_digits + str(first_digit), length=10, initial_weight=11)  # type: ignore
    assert (first_digit, second_digit) == (expected_first_digit, expected_second_digit)


def test_recursive_weighted_sum_calculation():
    """Ensure recursive sum is calculated correctly."""
    # digits 303, weights = 5, 4, 3
    result = Cpf._Cpf__recursive_weighted_sum("303", 5)  # type: ignore
    # 3*5 + 0*4 + 3*3 = 15 + 0 + 9 = 24
    assert result == 24


def test_recursive_weighted_sum_with_empty_string():
    """Ensure recursion base case returns 0 when digits are empty."""
    assert Cpf._Cpf__recursive_weighted_sum("", 5) == 0  # type: ignore
