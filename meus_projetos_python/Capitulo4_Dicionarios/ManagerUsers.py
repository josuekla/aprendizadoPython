from meus_projetos_python.Capitulo4_Dicionarios.Funcoes import *
usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)

    if opcao == "P":
        pesquisar(usuarios, input("Qual  usuário deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios, input("qual usuário deseja excluir?"))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()

        
        
