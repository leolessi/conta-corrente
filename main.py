from datetime import datetime
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


# inicio
conta_Leonardo = ContaCorrente("Leonardo", "123.123.123-12", 1234, 330033)
conta_Leonardo.consultar_saldo()


# deposito
print("-" * 20)
conta_Leonardo.depositar(33)
time.sleep(2)

# saque
print("-" * 20)
conta_Leonardo.sacar(333333333)
conta_Leonardo.sacar(133)

# tentando entrar no negativo
print("-" * 20)
time.sleep(2)
conta_Leonardo.sacar(37000)


# saldo final
print("-" * 20)
print("\nSaldo final: ")
conta_Leonardo.consultar_saldo()
conta_Leonardo.consultar_cheque_especial()

# consultar transacoes
print("-" * 20)
conta_Leonardo.consultar_transacoes()

# nova instancia
print("-" * 20)
conta_Teste = ContaCorrente("Nome do Teste", "123.123.123-33", 4321, 112233)
print(f"Saldo teste: {conta_Teste.consultar_saldo()}")

# transferencia
print("-" * 20)
conta_Leonardo.transferir(333, conta_Teste)

conta_Leonardo.consultar_saldo()
conta_Teste.consultar_saldo()

print("-" * 20)
conta_Leonardo.consultar_transacoes()

print("-" * 20)
conta_Teste.consultar_transacoes()
