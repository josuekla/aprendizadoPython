"""Este módulo e para preencher o inventário
"""


def preencher_inventario(lista):
    """preencher o inventário

    Args:
        lista (lista de equipamentos): _essa funçao devera criar uma lista
        e preencher com seus respectivos índices_
    """
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite 'S' para continuar: ").upper()


def exibir_inventario(lista):
    """_devera exibir ps equipamentos que está na listas_
    """
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])


def localizar_por_nome(lista):
    """ essa funcão vai localizar o equipamento por meio do input
    seo o input foi igual - o indice 1 que sao equipamentos, devera mostras as suas informações
    """
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])


def depreciar_por_nomme(lista, porc):
    """_deverá depreciar o produto com 10%

    Args:
        lista (lista de equipamento): 
        porc (_inteiro %_): 
    """
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])


def excluir_por_serial(lista):
    """excui o equipamento de acordo com o seu numero de Serial

    Args:
        lista (_type_): _description_

    Returns:
        string: retorna o equipamento que foi excluído
    """
    serial = int(input("Digite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos."


def resumir_valores(lista):
    """resume os os valores dos equipamentos

    Args:
        lista (_type_): Mostra o valor mais caro ,barato e as suas somas respectivamente
    """
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
