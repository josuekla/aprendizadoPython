nome = input('Digite o nome do Pacinte: ')
idade = int(input('Idade do paciente: '))
grave_dc = input('Suspeita de doença infecto-contagiosa:').upper()  #upper() faz com  que a resposta no input ser convertido para letras maiusculas
                                                                   #        e fique mais fáciel no coversão no if

if idade>=65 and grave_dc=='SIM':
    print('O paciente', nome, 'será direcionado para a sala AMARELA - COM priooridade')
elif idade < 65 and grave_dc=='SIM':
    print('O paciente', nome,'será direcionado para a sala AMARELA - SEM priooridade')
elif idade >=65 and grave_dc=='NAO':
    print("O paciente", nome,"será direcionado para a sala BRANCA - COM priooridade")
elif idade < 65 and grave_dc == 'NAO':
    print("O paciente", nome, "será direcionado para a sala BRANCA - SEM priooridade")
else :
    print('Responda a suspeita de doença - infectosa com SIM ou NAO')
# um "=" representa ATRIBUIÇÃO,dois "==" reprenta COMPARAÇÃO
# O "ELSE" SOMETE será executrado se a primeira e a segunda condição forem falsas
