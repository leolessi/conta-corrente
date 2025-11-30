class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimo = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado (R$ {self.caixa:,.2f})")
        else:
            print(f"Valor de caixa dentro dos requisitos (R$ {self.caixa:,.2f})")

    def fornecer_emprestimo(self, valor, cpf, juros):
        if self.caixa > 2 * valor:
            self.emprestimo.append(
                f"Empréstimo de R$ {valor:,.2f} (T.J {juros}) | Recebedor: {cpf}."
            )
            self.caixa -= valor
        else:
            print("Empréstimo indisponível. Dinheiro em caixa não disponível.")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, telefone, cnpj, site):
        super().__init__(telefone, cnpj, numero="0001")
        self.site = site
        self.caixa = 2500000
        self.caixa_paypal = 0

    # metodos de tranferencia paypal <-> caixa da agencia
    def depositar_paypal(self, valor):
        if valor <= self.caixa:
            self.caixa -= valor
            self.caixa_paypal += valor
        else:
            print(
                f"Caixa principal insuficiente para transferência (R$ {self.caixa:,.2f})"
            )

    def sacar_paypal(self, valor):
        if valor >= self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print(
                f"Caixa do paypal insuficiente para transferência (R$ {self.caixa:,.2f})"
            )


class AgenciaSilver(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero="0002")
        self.caixa = 5000000


class AgenciaBlack(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero="0003")
        self.caixa = 15000000


# print("-" * 30)

agencia_virtual = AgenciaVirtual(
    11911111111,
    1000000001,
    "www.agenciavirtual.com.br",
)
agencia_virtual.verificar_caixa()
agencia_virtual.depositar_paypal(500000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia_silver = AgenciaSilver(11922222222, 2000000002)
agencia_black = AgenciaBlack(11933333333, 3000000003)
