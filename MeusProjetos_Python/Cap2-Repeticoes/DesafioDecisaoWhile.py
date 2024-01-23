resposta ="SIM"
while resposta == "SIM":
    seu_nivel = input('Digite o seu Nível:').upper()
    if seu_nivel == "ADM" or seu_nivel ==  'USR':
        genero = input('Digite o seu gênero:').upper()
        if seu_nivel == 'ADM':
            if genero == "FEMININO":
                print('Olá administradora!')
            else :
                print('Olá administrador!')
        else:
            if genero == 'FEMININO':
                print("Ola usuária")
            else:
                print("Olá usuário")
    elif seu_nivel == 'GUEST':
        print('Olá visitante!')
    else:
        print('Olá desconhecido(a)')
    resposta = input('Digite SIM para contitnuar: ').upper()
