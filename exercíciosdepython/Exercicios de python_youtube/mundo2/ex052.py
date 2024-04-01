num = int(input("Digite um número: "))

divisores = []

for i in range(2, num):
    if num % i == 0:
        divisores.append(i)

if not divisores and num > 1:
    print(f"{num} é um número PRIMO.")
else:
    print(f"{num} não é um número primo.")

print(f"Esse número: {num} foi divisível por: {divisores}")