from datetime import date
atual = date.today().year

jovem = 0
idadeAv = 0

for ano in range(1,8):
    age = int(input(f"Digite o {ano}º ano de nascimento: "))
    idade = atual -  age
    print(idade)
    if idade < 21:
        jovem += 1
    else:
        idadeAv += 1

print(f"A todo temos {jovem} menores de idade\n"
f"E {idadeAv} com maiores de idades ")