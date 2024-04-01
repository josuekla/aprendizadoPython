km = float(input("Quantos Km pecorreu? KM"))
dias = int(input("Quanto dias você pecorreu?"))
conversao_km = km * 0.15
custodia = dias * 60 + conversao_km
print(f"Você pecorreu {km}KM em {dias} dias e o total custo será de: {custodia}")
