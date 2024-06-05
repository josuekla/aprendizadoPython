num = int(input("Digite um número inteiro: "))
escolha = int(input("Escolha umas das bases para conversão: "
'''\n[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))
if escolha == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif escolha == 2:
    print(f"{num} Convertido para OCTAL é igual a {oct(num)[2:]}")
elif escolha == 3:
    print(f"{num} Convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida")