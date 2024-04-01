from datetime import date
ano = int(input(f"Informe a sua data de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - ano
print(f"Você que nasceu em {ano} e tem {idade} anos de idade\n")
if idade <= 9:
    print("Você pertence a categoria MIRIM.")

elif idade <= 14:
    print("Você pertence a categoria INFANTIL.")

elif idade <= 19:
    print("Você pertence a categoria JÚNIOR.")

elif idade <= 25:
    print("Você pertence a categoria SÊNIOR.")
    
else:
    print("Você pertence a categoria MASTER.")