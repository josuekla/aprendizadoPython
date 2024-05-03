maior = 0
man = 0
womam = 0

while True:
    print("--"*10)
    print("Cadastre uma pessoa")
    print("--"*10)

    age = int(input("idade: "))
    if age >= 18:
        maior += 1
    sex = input("Sexo: [M/F] ").upper()
    if sex == "M" :
        man += 1
    elif sex == "F" and age < 20:
        womam += 1
    print("--"*10)
    resp = input("Quer continuar? [S/N]").upper()
    if resp != "S":
        break

print(f"Ao todo têm {maior} pessoas com maior de idade.")
print(f"Foram cadastrado {man} homens.")
print(f"E ao todo foram {womam} mulheres cadastradas menores de 20 anos.")