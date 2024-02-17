'''
1 número do usuário
2 multiplicar da direita para esquerda o número do usuário e exibir na tela
3 deve ser um número inteiro e positivo
4 a fatorial/resultado da multiplicação do número
5
- input numero do usuario
- if numero>0
  if numero = inteiro
  fatorial = 1

  loop 1 a numero
  fatorial = fatorial * numero
  print(fatorial)
'''

num= int(input('Digite o númeoro fatorial: '))
if num > 0:
    fatorial=1
    for itens in range(1,num+1):
        fatorial*= itens
    print(fatorial)
