nome = input("Digite o seu nome: ")
idade = int(input('Digite a idade: '))
doenca_infec = input("Suspeita de doença infectocontagiosa? ").upper()
#PRIMEIRO PROBLEMA RESOLVIDO
while doenca_infec != 'SIM' and doenca_infec != 'NAO':
    print('Responda  com SIM ou NAO')
    doenca_infec = input('Suspeita de doença infectocontagiosa? ').upper()

if doenca_infec == "SIM":
    print('Encaminhe o pacienta para a sala AMARELA')
else :
    print('Encaminhe o pacienta para a sala BRANCA')
#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65 :
    print('Paciente COM prioridade')
else:
    genero = input('Digite o seu gênero do paciente :').upper()
    if genero == 'FEMININO' and idade>10:
        gravidez = input('estar grávida? ').upper()
        if gravidez == "SIM":
            print('Paciente COM prioridade')
        else:
            print('Paciente SEM prioridade')

    else:
        print('Paciente SEM prioridade')
