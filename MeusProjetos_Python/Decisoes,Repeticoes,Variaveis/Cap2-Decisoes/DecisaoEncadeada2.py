nome=input('Digite o seu nome: ')
idade=int(input("Digite a idade: "))
doenca_infec=input('Suspeita de doença infectocontagiosa? ').upper()

#PRIMEIRO PROBLEMA RESOLVIDO
if doenca_infec == 'SIM':
    print('Encaminhe o pacienta para a sala AMARELA')
elif doenca_infec == 'NAO':
    print('Encaminhe o pacienta para a sala BRANCA')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65 :
    print('Paciente COM prioridade')
else:
    genero=input('Digite o seu gênero do paciente :').upper()
    if genero=='FEMININO' and idade>10:
        gravidez= input('estar grávida? ').upper()
        if gravidez=="SIM":
            print('Paciente COM prioridade')
        else:
            print('Paciente SEM prioridade')

    else:
        print('Paciente SEM prioridade')
