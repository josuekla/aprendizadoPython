inventario = {}


def registrar_ativo():
    resposta = "S"
    while resposta == "S":
        numero_patrimonial = input("Digite o número patrimonial: ")
        data_atualizacao = input("Digite a data da última atualização: ")
        descricao = input("Digite a descrição: ")
        departamento = input("Digite o departamento: ")
        inventario[numero_patrimonial] = [data_atualizacao, descricao, departamento]
        resposta = input("Digite <S> para continuar: ").upper()


def persistir_em_arquivo():
    with open("inventario.csv", "a") as inv:
        for chave, valor in inventario.items():
            linha = f"{chave};{valor[0]};{valor[1]};{valor[2]}\n"
            inv.write(linha)
        print("Dados persistidos com sucesso!")


def exibir_ativos_armazenados():
    with open("inventario.csv", "r") as inv:
        print(inv.read())


while True:
    print("\nOpções:"
          "\n<1> para registrar um ativo"
          "\n<2> para persistir em arquivo"
          "\n<3> para exibir ativos armazenados")
    opcao = int(input("Digite sua escolha: "))
    if opcao == 1:
        registrar_ativo()
    elif opcao == 2:
        persistir_em_arquivo()
    elif opcao == 3:
        exibir_ativos_armazenados()
    else:
        print("Opção inválida. Digite novamente.")
