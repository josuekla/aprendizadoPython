print("DIGITE APENAS NÚMEROS PARES")
soma = 0
cont = 0
for a in range(1, 7):
    num = int(input("Digite o {} valor: ".format(a)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print(f"A soma de {cont} números PARES foi ao todo foi: {soma}")