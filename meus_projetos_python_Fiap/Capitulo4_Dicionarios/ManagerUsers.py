from meus_projetos_python_Fiap.Capitulo4_Dicionarios.Funcoes import *
usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)

    if opcao == "P":
        pesquisar(usuarios, input("Qual  login deseja pesquisar? ").upper())
    if opcao == "E":
        excluir(usuarios, input("Qual login deseja excluir?").upper())
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()



