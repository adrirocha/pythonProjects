import re
from validate_docbr import CPF
import requests
from datetime import datetime

class TipoAnimal:
    @staticmethod
    def cadastro(tipo_animal, nome_dono, cep, cpf, numero_telefone):
        if tipo_animal.upper() == 'GATO':
            return Gato(nome_dono, str(cep), str(cpf), str(numero_telefone))
        if tipo_animal.upper() == 'CAO' or tipo_animal.upper() == 'CACHORRO' or tipo_animal.upper() == 'CÃO':
            return Cachorro(nome_dono, str(cep), str(cpf), str(numero_telefone))
        else:
            raise ValueError('Não atendemos o tipo do animal especificado: {}.' .format(tipo_animal))

class Gato:
    def __init__(self, nome_dono, cep, cpf, numero_telefone):
        self._tipo_animal = 'Gato'
        self._nome_dono = nome_dono.title()
        self._momento_cadastro = datetime.today()
        if self._valida_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError('O CPF não é válido.')
        if self._valida_cep(cep):
            self._cep = cep
        else:
            raise ValueError('O CEP não é válido.')
        if self._valida_telefone(numero_telefone):
            self._numero_telefone = numero_telefone
        else:
            raise ValueError('O número de telefone não é valido.')


    def __str__(self):
        return f'Dono: {self._nome_dono}, Tipo do animal: {self._tipo_animal}, CPF: {self.format_cpf()}, Endereço: {self.get_cep()}, Contato: {self.format_telefone()}'

    def _valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)

    def _valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}' .format(self._cep[:5],self._cep[5:])

    def get_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/' .format(self._cep)
        get = requests.get(url)
        dados = get.json()
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

    def _valida_telefone(self, numero_telefone):
        numero_telefone = numero_telefone.replace('-', '')
        if len(numero_telefone) > 14:
            raise ValueError('Número de telefone ultrapassou o máximo de caracteres.')
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, numero_telefone)
        if resposta:
            return True
        else:
            return False

    def format_telefone(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self._numero_telefone)
        numero_formatado = '+{}({}){}-{}' .format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado

    def format_data(self):
        data_formatada = self._momento_cadastro.strftime('%d/%m/%y %H:%M')
        return data_formatada

class Cachorro:
    def __init__(self, nome_dono, cep, cpf, numero_telefone):
        self._tipo_animal = 'Cachorro'
        self._nome_dono = nome_dono.title()
        self._momento_cadastro = datetime.today()
        if self._valida_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError('O CPF não é válido.')
        if self._valida_cep(cep):
            self._cep = cep
        else:
            raise ValueError('O CEP não é válido.')
        if self._valida_telefone(numero_telefone):
            self._numero_telefone = numero_telefone
        else:
            raise ValueError('O número de telefone não é valido.')


    def __str__(self):
        return f'Dono: {self._nome_dono}, Tipo do animal: {self._tipo_animal}, CPF: {self.format_cpf()}, Endereço: {self.get_cep()}, Contato: {self.format_telefone()}'

    def _valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)

    def _valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}' .format(self._cep[:5],self._cep[5:])

    def get_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/' .format(self._cep)
        get = requests.get(url)
        dados = get.json()
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

    def _valida_telefone(self, numero_telefone):
        numero_telefone = numero_telefone.replace('-', '')
        if len(numero_telefone) > 14:
            raise ValueError('Número de telefone ultrapassou o máximo de caracteres.')
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, numero_telefone)
        if resposta:
            return True
        else:
            return False

    def format_telefone(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self._numero_telefone)
        numero_formatado = '+{}({}){}-{}' .format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado

    def format_data(self):
        data_formatada = self._momento_cadastro.strftime('%d/%m/%y %H:%M')
        return data_formatada










