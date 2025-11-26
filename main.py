from datetime import datetime
from random import randint
import pytz
import time


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_br = datetime.now(fuso_BR)
        return horario_br.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f"{self._nome} | Seu saldo atual: R$ {self._saldo:,.2f}")

    def consultar_transacoes(self):
        print(f"Historico de transacoes: ", *self._transacoes, sep="\n")

    # "metodo auxiliar" para o metodo sacar | metodo que sera usado apenas dentro da classe
    def _limite_negativo(self):
        self._limite = -1000
        return self._limite

    def consultar_cheque_especial(self):
        print(f"Seu limite de cheque especial: R$ {self._limite_negativo():,.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append(
            (
                f"Valor: +{valor} | Saldo: {self._saldo:,.2f} | Data/Hora: {ContaCorrente._data_hora()}"
            )
        )
        self.consultar_saldo()

    def sacar(self, valor):
        if self._saldo - valor < self._limite_negativo():
            print(f"Saldo insuficiente para realizar saque.")
        else:
            self._saldo -= valor
            self._transacoes.append(
                (
                    f"Valor: -{valor} | Saldo: {self._saldo:,.2f} | Data/hora: {ContaCorrente._data_hora()}"
                )
            )

        self.consultar_saldo()

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append(
            (
                f"Valor: -{valor} | Saldo: {self._saldo:,.2f} | Data/hora: {ContaCorrente._data_hora()}"
            )
        )
        conta_destino._saldo += valor
        conta_destino._transacoes.append(
            (
                f"Valor: +{valor} | Saldo: {conta_destino._saldo:,.2f} | Data/hora: {ContaCorrente._data_hora()}"
            )
        )


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_br = datetime.now(fuso_BR)
        return horario_br

    @staticmethod
    def gerar_numero_cartao():
        numero_cartao = randint(1000000000000000, 9999999999999999)
        return numero_cartao

    @staticmethod
    def gerar_validade():
        mes_validade = CartaoCredito._data_hora().month
        ano_validade = CartaoCredito._data_hora().year
        return f"{mes_validade}/{ano_validade + 4}"

    def __init__(self, titular, conta_corrente):
        self.titular = titular
        self.numero_cartao = CartaoCredito.gerar_numero_cartao()
        self.validade = CartaoCredito.gerar_validade()
        self.cod_seguranca = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


# inicio
conta_Leonardo = ContaCorrente("Leonardo", "123.123.123-12", 1234, 330033)

# instancia do cartao
cartao_Leonardo = CartaoCredito("Leonardo", conta_Leonardo)


print(conta_Leonardo.cartoes[0].titular)
print(cartao_Leonardo.numero_cartao)
print(cartao_Leonardo.validade)
print(cartao_Leonardo.cod_seguranca)
