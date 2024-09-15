alunos = dict()

def adicinar_aluno(nome_aluno, nota1, nota2):
    alunos[nome_aluno] = {'Português': nota1, "Matemática":nota2}

def atualizar(nome_aluno, nota_atualizada1, nota_atualizada2):
    if nome_aluno in alunos:
        alunos[nome_aluno] = {'Português': nota_atualizada1, 'Matemática': nota_atualizada2}
    else:
        return 'informe um nome válido'
    
def remover(nome_aluno):
    if nome_aluno in alunos:
        alunos.pop(nome_aluno)

while True:
    nome_aluno = input('Adicione aluno:')
    nota1 = input('Primeira nota:')
    nota2 = input('Segunda nota:')
    adicinar_aluno(nome_aluno, nota1 , nota2)
    r = input('Deseja adicionar mais alunos: <S> <N>').upper()
    if r in 'Nn':
        break
    elif r != 'S':
        print('Digite algum Sim ou Não!')
    print(alunos)

print('Área de atualização de notas')

atualizar(input('nome do aluno: '), input('Primeira nota atualizada: '), input('Segunda nota atualizada: '))  
print(alunos)  
remover(input('Nome do aluno para remover: '))
print(alunos)