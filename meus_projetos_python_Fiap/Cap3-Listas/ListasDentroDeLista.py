inventario = []

resposta = 'S'

# Adicionar item no inventário
while resposta == 'S':
    equipamento = [input('Equipamento: '),
                   float(input("Valor:  ")),
                   int(input("Númeor serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite 'S' para continuar: ").upper()
    print(inventario)
# Mostra para o usuário a sua lista de itens
for elemento in inventario:
    print("Nome...........:", elemento[0])
    print("Valor..........:", elemento[1])
    print("Serial.........:", elemento[2])
    print("Departamento...:", elemento[3])
# Faz a busca do item desejado pelo usuário
busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..........:", elemento[1])
        print("Serial.........:", elemento[2])
# Deprecia o item escolhido pelo usuário
depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo.......:", elemento[1])
        elemento[1] *= 0.9
        print("Novo valor: ", elemento[1])
# Excluir itens escolhido pelo usuário de acordo com o número do serial
serial = int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario.copy():
    if elemento[2] == serial:
        inventario.remove(elemento)

# Mostra a nova lista atualizada
for elemento in inventario:
    print("Nome...........:", elemento[0])
    print("Valor..........:", elemento[1])
    print("Serial.........:", elemento[2])
    print("Departamento...:", elemento[3])
# RESUMI OS VALORES
# Mostra o equipamento mais cara, mais barato e a soma de todos os equipamentos-
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O total de equipamento é de : ', sum(valores))
