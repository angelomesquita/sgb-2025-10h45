"""
    Regras de validação de CPF
        1. O CPF tem 11 dígitos numéricos
        2. Os 9 primeiros dígitos são usados para calcular os 2 últimos (dígitos verificadores)
        3. O primeiro dígito verificador (10º dígito) é calculado multiplicando-se o 9 primeiros
           dígitos por pesos decrescentes de 10 a 2.
        4. O segundo dígito verificador (11º dígito) é calculado com os 9 primeiros dígitos + o
           primeiro dígito verificador, usando pesos de 11 a 2.
        5. A fórmula do dígito verificador é:
            - Soma dos produtos dos dígitos * pesos
            - Resto da divisão da soma por 11
            - Se o resto for menor que 2, o dígito é 0, senão é 11 - resto
        Exemplo:
            -  415.081.330-??
            - primeiro dígito veficicador:
                - 4x10 + 1x9 + 5x8 + 0x7 + 8x6 + 1x5 + 3x4 + 3x3 + 0x2
                - 40 + 9 + 40 + 0 + 48 + 5 + 12 + 9 + 0 = 163
                - 163 / 11 = 14 resto 9 | 11 - 9 = 2
                -  451.081.330-2?
            - segundo dígito verificador:
                - 4x11 + 1x10 + 5x9 + 0x8 + 8x7 + 1x6 + 3x5 + 3x4 + 0x3 + 2x2
                - 44 + 10 + 45 + 0 + 56 + 6 + 15 + 12 + 0 + 4 = 192
                - 192 / 11 = 17 resto 5 | 11 - 5 = 6
                - 451.081.330-26
"""


class Cpf:
    _CPF_LENGTH = 11

    @staticmethod
    def validate(cpf: str) -> bool:
        cleaned_cpf = Cpf.clean(cpf)
        return cleaned_cpf.isdigit() and len(cleaned_cpf) == Cpf._CPF_LENGTH

    @staticmethod
    def clean(cpf: str) -> str:
        """ Removes non-numeric characters from the CPF """
        return ''.join(filter(str.isdigit, cpf))  # TODO: Lição 11 - Manipulação de Strings
