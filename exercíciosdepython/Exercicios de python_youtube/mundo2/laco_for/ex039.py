from datetime import date
ano = int(input("Ano de nascimento: "))
data_atual = date.today().year
idade = data_atual - ano
print(f"Você que nasceu em {ano} tem {idade} anos de idade.")
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE")
elif idade > 18:
    tempo = idade - 18
    falta = ano + 18
    print(f"Você já deveria ter se alistado no exército há {tempo} ano(s)"
    f"\nSeu alistamento foi em {falta}.")
else:
    tempo = 18 - idade
    falta = 18 + ano
    print(f"Você tem {idade} e ainda não precisa se alistar no exército,\n"
    f"faltam {tempo} ano para você se alistar.\n"
    f"Seu alistamento ocorrerá em {falta}")