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
