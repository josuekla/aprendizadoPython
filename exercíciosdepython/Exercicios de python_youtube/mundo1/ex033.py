n1 = int(input("Informe o primerio número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f"MAIOR: {maior}")
print(f"MENOR: {menor}")