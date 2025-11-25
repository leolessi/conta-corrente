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
        self.nome = nome
        self.cpf = cpf
        self.saldo = 33100
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print(f"Seu saldo atual: R$ {self.saldo:,.2f}")

    def consultar_transacoes(self):
        print(f"Historico de transacoes: ")
        for transacao in self.transacoes:
            print(transacao)

    # "metodo auxiliar" para o metodo sacar | metodo que sera usado apenas dentro da classe
    def _limite_negativo(self):
        self.limite = -1000
        return self.limite

    def consultar_cheque_especial(self):
        print(f"Seu limite de cheque especial: R$ {self._limite_negativo():,.2f}")

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(
            (
                f"Valor: +{valor} | Saldo: {self.saldo:,.2f} | Data/Hora: {ContaCorrente._data_hora()}"
            )
        )
        self.consultar_saldo()

    def sacar(self, valor):
        if self.saldo - valor < self._limite_negativo():
            print(f"Saldo insuficiente para realizar saque.")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append(
                (
                    f"Valor: -{valor} | Saldo: {self.saldo:,.2f} | Data/hora: {ContaCorrente._data_hora()}"
                )
            )
            self.consultar_saldo()


# inicio
conta_Leonardo = ContaCorrente("Leonardo", "123.123.123-12", 1234, 330033)
conta_Leonardo.consultar_saldo()

# deposito
conta_Leonardo.depositar(33)
conta_Leonardo.consultar_saldo()

time.sleep(2)
# saque
conta_Leonardo.sacar(333333333)
conta_Leonardo.sacar(133)

# tentando entrar no negativo
time.sleep(2)
conta_Leonardo.sacar(37000)


# saldo final
print("\nSaldo final: ")
conta_Leonardo.consultar_saldo()
conta_Leonardo.consultar_cheque_especial()

# consultar transacoes
print()
conta_Leonardo.consultar_transacoes()
