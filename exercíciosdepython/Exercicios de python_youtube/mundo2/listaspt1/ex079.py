lista = []
soma = 0 

resp = 'S'
while resp == 'S':
    n = int(input("Digite um valor:"))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
        print(lista)
    else:
        print("Valor já escolhido, adicione outro ...")
        print(lista)

    resp = input("Deseja continuar? [S/N]").upper()

    
lista.sort()
print(lista)



    # COMO EU ESTAVA TENTANDO FAZER:

    # lista.append(input("Digite um número:"))
    # soma +=1
    # for i in lista:
    #     if i not in lista:
            
    #         print(lista)
    #     elif i in lista:

    # # if lista
