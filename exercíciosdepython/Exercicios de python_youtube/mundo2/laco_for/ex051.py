num = int(input("Digite um valor: "))
razao = int(input("Digite a razão: "))
decimo = num + (10 - 1) * razao
for seq in range(num, decimo, razao):
    print(seq , end = " → ")
print("acabou")

