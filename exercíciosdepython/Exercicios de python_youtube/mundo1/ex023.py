numero = int(input("Informe um numero: "))
print(f"Analisando o numero {numero}")
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
#print(separar)
print(f"unidade: {unidade}")
print(f"centena: {dezena}")
print(f"centena: {centena}")
print(f"milhar: {milhar}")