"""  teste de projeto
"""
from meus_projetos_python_Fiap.Cap3_Funcoes.indetificacoesdefuncoes import *

minhaLista = []
print("Preenchendo")
preencher_inventario(minhaLista)
print("Exibindo")
exibir_inventario(minhaLista)

print("Pesquisando")
localizar_por_nome(minhaLista)
print("Alterando")
depreciar_por_nomme(minhaLista, 20)

print("Excluindo")
print(excluir_por_serial(minhaLista))
exibir_inventario(minhaLista)

print("Resumindo")
resumir_valores(minhaLista)
