class Cpf:

    _CPF_LENGTH = 11

    @staticmethod
    def validate(cpf: str) -> bool:
        # TODO: Missing validation with check digit calculations.
        # TODO: Lição 9 - Recursividade
        cleaned_cpf = Cpf.clean(cpf)
        return cleaned_cpf.isdigit() and len(cleaned_cpf) == Cpf._CPF_LENGTH

    @staticmethod
    def clean(cpf: str) -> str:
        """ Removes non-numeric characters from the CPF """
        return ''.join(filter(str.isdigit, cpf))  # TODO: Lição 11 - Manipulação de Strings
