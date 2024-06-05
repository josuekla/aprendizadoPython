print("{:=^40}".format("LOJAS JK"))
compras = float(input(("Preço das compras: R$")))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/chegue
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão """)
opcao = int(input("Qual é a sua opção? "))

op01 = compras * 0.9
op02 = compras * 0.95
op04 = compras * 1.2

if opcao == 1:
    print(f"Sua compra de R${compras} vai custar R${op01} no final.")
elif opcao == 2:
    print(f"Sua compra de R${compras} vai custar agora R${op02}.")
elif opcao == 3:
    print(f"Suas compras custou R${compras}, não sofreu alterações.")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = op04 / parcelas
    print(f"Suas compras será parcelada em {parcelas}x de {juros} COM JUROS\n"
    f"Sua compra de {compras} vai custar agora R${op04} no final.")
else:
    print("DIGITE UMA OPÇÃO VÁLIDA!")

