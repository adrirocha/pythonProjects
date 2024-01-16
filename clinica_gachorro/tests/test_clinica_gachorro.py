from clinica_gachorro import TipoAnimal
import pytest
from pytest import mark

class TestClass:
    def test_quando_formata_numero_de_telefone_recebe_555197891377_retorna_numero_formatado(self):
        entrada = '555197891377'
        esperado = '+55(51)9789-1377'

        teste = TipoAnimal.cadastro('gato', 'Teste', '08062110', 96387688868, entrada)
        resultado = teste.format_telefone()

        assert resultado == esperado

    def test_quando_formata_cpf_96387688868_retorna_cpf_formatado(self):
        entrada = '96387688868'
        esperado = '963.876.888-68'

        teste = TipoAnimal.cadastro('cao', 'Teste', '08062110', entrada, 555197891377)
        resultado = teste.format_cpf()

        assert resultado == esperado

    @mark.cep
    def test_quando_formata_cep_05085050_retorna_cep_formatado(self):
        entrada = '05085050'
        esperado = '05085-050'

        teste = TipoAnimal.cadastro('cachorro', 'Teste', entrada, 96387688868, 555197891377)
        resultado = teste.format_cep()

        assert resultado == esperado

    @mark.cep
    def test_quando_get_cep_retorna_endereco_certo(self):
        entrada = '05085050'
        esperado = ('Vila Bela Aliança', 'São Paulo', 'SP')

        teste = TipoAnimal.cadastro('gato', 'Teste', entrada,  96387688868, 555197891377)
        resultado = teste.get_cep()

        assert resultado == esperado

    def test_quando_tenta_cadastrar_tipo_de_animal_diferente_deve_retornar_valueerror(self):
        with pytest.raises(ValueError):
            entrada = 'gorila'

            resultado = TipoAnimal.cadastro(entrada, 'Teste', '05075050', 96387688868, 555197891377)

            assert resultado







