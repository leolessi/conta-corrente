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


agencia_1 = Agencia(11911112222, 2000000000, 1234)
agencia_1.verificar_caixa()

agencia_1.caixa = 123123123123123
agencia_1.verificar_caixa()

agencia_1.fornecer_emprestimo(23123, 12312312312, 0.02)
agencia_1.verificar_caixa()

agencia_1.adicionar_cliente("Leonardo", 11122233344, 10000)
print(agencia_1.clientes)
