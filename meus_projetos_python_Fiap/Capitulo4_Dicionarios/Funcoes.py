def perguntar():
    resposta = input("O deseja realizar\n" +
                     "<I> Para inserir um usuário\n" +
                     "<P> Para pesquisar um usuário\n" +
                     "<E> Para excluir um usuário\n" +
                     "<L> Para listar um usuário: ").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada:").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("O nome é: ", lista[0])
        print("Última data de acesso: ", lista[1])
        print("Última estação: ", lista[2])


def excluir(dicionario, chave):
    if chave in dicionario:
        valor = dicionario.pop(chave)
        print("Objeto eliminado:", valor)
    else:
        print("Chave não encontrada")



def listar(dicionario):
    for chave, valor in dicionario.items():
        print("OBJETO.........")
        print("Login: ", chave)
        print("Dados: ", valor)
