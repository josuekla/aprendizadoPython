velhoM = 0
nomeM = ""
nomeF = 0
idade_total = 0

for c in range(1,5):
    print(f"-----{c}º PESSOA-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    idade_total += idade

    sex = str(input("Sexo: [M/F]")).strip().upper()
    if sex == "M" :
        if idade > velhoM:
            velhoM = idade
            nomeM = nome
    elif sex == "F" :
        if idade < 20:
            nomeF += 1





media_age = idade_total / 4
print(f"A média de idade desse grupo foi de {media_age}.")
print(f"O {nomeM} é o homem mais velho com {velhoM} anos de idade. ")
print(f"Ao todo são {nomeF} mulheres com menos de 20 anos.")
