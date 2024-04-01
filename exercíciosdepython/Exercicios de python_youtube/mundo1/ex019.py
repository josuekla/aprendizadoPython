from random import choice
lista = []
n1 = lista.append(input("Digite o PRIMEIRO nome: "))
n2 = lista.append(input("Digite o SEGUNDO nome: "))
n3 = lista.append(input("Digite o TERCEIROnome: "))
n4 = lista.append(input("Digite o QUARTO nome: "))

sorteado = choice(lista)
print(F"Alunos {lista} Serão sorteado: "
        f"\nAluno escolhido foi: {sorteado}")
