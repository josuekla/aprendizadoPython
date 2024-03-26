n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda  nota:"))
media = (n1 + n2) / 2
print("A sua nota foi de:", media)
if media < 5:
    print("Esse aluno está REPROVADO")
elif 5 <= media <= 6.9:
    print("Esse aluno está de RECUPERAÇÃO")
else:
    print("Esse aluno está APROVADO")