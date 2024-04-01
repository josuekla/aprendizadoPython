distancia = float(input("Digite a distância da sua viagem em KM: "))
if distancia <= 200:
    custo = distancia * 0.50
    print(f"A sua viagem com a distância de {distancia}KM, custará: {custo} Reais")
else:
    custo = distancia * 0.45
    print(f"A sua viagem com a distância de {distancia}KM, custará: {custo} Reais")