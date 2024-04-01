speed = float(input("Digite a sus velocidade: KM "))
custo = (speed - 80) * 7
if speed > 80:
    print(f"Foi MULTADO! Total a pagar será de: {custo}")
else:
    print("Tenha um ótimo dia! ande com segurança")