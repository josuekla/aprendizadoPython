peso = float(input("Digite o seu peso:KG "))
altura = float(input("Digite a sua altura:CM "))
calculo = peso / (altura ** 2)
print(f"O IMC desta pessoa é de {calculo:.2f}")
if calculo < 18.5:
    print("Você está ABAIXO DO PESO!.")
elif 18 < calculo <= 25:
    print("VOcê está no PESO IDEAL.")
elif 25 < calculo <= 30:
    print("Você está SOBREPESO.")
elif 30 < calculo <= 40:
    print("Você está na OBESIDADE.")
else:
    print("Vcê está na OBESIDADE MÓRBIDA!")