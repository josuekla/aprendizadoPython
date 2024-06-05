seu_nivel=input('Digite o seu Nível:').upper()
if seu_nivel== "ADM" or seu_nivel=='USR':
    genero=input('Digite o seu gênero:').upper()
    if seu_nivel=='ADM':
        if genero=="feminino":
            print('Olá administradora!')
        else :
            print('Olá administardor')
    else:
        if genero=='FEMININO':
            print("Ola usuária")
        else:
            print("Olá usuário")
elif seu_nivel=='GUEST':
    print('Olá visitante!')
else:
    print('Olá desconhecido(a)')








#meu jeito --->
#    print('Olá administrador!')
#elif seu_nivel== "ADM" and genero=="FEMININO":
#    print('Olá administradora!')
#elif seu_nivel == "USR" and genero == "MASCULINO":
#    print('Olá usuário!')
#elif seu_nivel == "USR" and genero == "FEMININO":
#    print('Olá usuária!')
#elif seu_nivel == "GUEST":
#    print('Olá visitante!')
#else :
#    print('Olá desconhecido(a)')


