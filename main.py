from contas_bancos import ContaCorrente, CartaoCredito

# inicio
conta_Leonardo = ContaCorrente("Leonardo", "123.123.123-12", 1234, 330033)

# instancia do cartao
cartao_Leonardo = CartaoCredito("Leonardo", conta_Leonardo)


print(conta_Leonardo.cartoes[0].titular)
print(cartao_Leonardo.numero_cartao)
print(cartao_Leonardo.validade)
print(cartao_Leonardo.cod_seguranca)

print(cartao_Leonardo.senha)
cartao_Leonardo.senha = "4321"
print(cartao_Leonardo.senha)
