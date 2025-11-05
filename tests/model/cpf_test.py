from model.cpf import Cpf


def test_clean_removes_non_digits():
    """Ensure non-digits characters are removed from CPF."""
    cpf = "111.111.111-11"
    cleaned = Cpf.clean(cpf)
    assert cleaned == '11111111111'
