nome=input('Digite um funcionário:')
empresa=input('Digite a instituição: ')
qtde_funcionarios=int(input('Digite a qtde de funcionários:'))
mediaMensalidade=float(input('Digite a média da mensalidade:'))

print(nome,'trabalha na empresa',empresa)
print('possui:',qtde_funcionarios,'funcionarios.')
print('A média da mensalidade é de:' + str(mediaMensalidade))
print('=====================Verificando os tipos de dados abaixo: ================================')
print('O tipo de dado da variavel[nome] é:',type(nome))
print('O tipo de dado da variavel[empresa] é:',type(empresa))
print('O tipo de dado da variavel[qtde_funcionarios] é:',type(qtde_funcionarios))
print('O tipo de dado da variavel[mediaMensalidade] é:',type(mediaMensalidade))

