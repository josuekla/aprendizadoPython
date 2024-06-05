r = input("Digite o seu sexo: M/F".upper()).upper()
print(r)
while r not in "MF":
    r = input("Digite um valor válido").upper()
print("Valor válido")



