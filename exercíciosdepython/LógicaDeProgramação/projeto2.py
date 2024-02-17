'''
1. o chute inicial aleatório de 1 a 10 e o numero chutado do usuário de 1-10
2. se o numero do usuario estiver correto deve exibir na tela que acertou se estiver
errado não acertou e da algumas dicas
3. tem quer ser numeros de 1 a 10
4. se acerta ---> acertou
   se o numero for abaixo que o valo0r aleatório ---> tente um valor mais alto
   se o numero for cima que o valo0r aleatório ---> tente um valor mais baixo
5.
input digite o numero aleátorio
escolher um numero de 1 a 10
loop de 1 a  10
if numero = loop
    print acertou
elif numero > loop
    print tente um número mais baixo
elif numero < loop
    print tente um número mais alto
else
    print digite um número de 1 a 10
'''

import random
valor_aleatorio = random.randint(1,100)
acertou = False
while acertou==False:
    chute = int(input("Digite o  seu chute entre 1 à 100: "))
    if chute > 0 and chute < 101:

        if chute > valor_aleatorio:
            print("O seu chute foi MAIOR do que o valor gerado.")
        elif chute < valor_aleatorio:
            print("O seu chute foi MENOR do que o valor gerado.")
        elif chute == valor_aleatorio:
            acertou = True
            print('Parabéns, Você acertou!!')
    else:
        print('TEM QUE SER UM NÚMERO ENTRE 1 à 100!')