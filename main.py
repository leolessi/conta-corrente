class ContaCorrente:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        return self.saldo

    def limite_negativo(self):
        self.limite = -1000
        return self.limite

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo - valor > self.limite_negativo():
            self.saldo -= valor
            return self.saldo
        else:
            print(f"Saldo insuficiente para sacar esse valor!")
            return self.saldo


conta_Leonardo = ContaCorrente("Leonardo", "123.123.123-12")

saldo_Leonardo = conta_Leonardo.consultar_saldo()
print("Saldo atual: R$ {:,.2f}".format(saldo_Leonardo))

valor_deposito = 500
conta_Leonardo.depositar(valor_deposito)
saldo_Leonardo = conta_Leonardo.consultar_saldo()
print(
    "Deposito de R$ {:,.2f}. Saldo atual: R$ {:,.2f}".format(
        valor_deposito, saldo_Leonardo
    )
)

valor_saque = 3000
conta_Leonardo.sacar(valor_saque)
saldo_Leonardo = conta_Leonardo.consultar_saldo()
print(
    "Saque de R$ {:,.2f}. Saldo atual: R$ {:,.2f}".format(valor_saque, saldo_Leonardo)
)


valor_saque = 8000
conta_Leonardo.sacar(valor_saque)
