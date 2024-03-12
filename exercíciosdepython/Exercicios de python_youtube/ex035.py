print("_-_-" * 13)
print("Calcular se o seus segmentos podem formar um triângulo".upper())
print("_-_-" * 13)
print("\n")
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))
if a < b + c and b < a+c and c < a+b :
    print("Esses segmentos podem formar um triângulo!")
else:
    print("Esses segmentos NÃO podem formar um triângulo")
