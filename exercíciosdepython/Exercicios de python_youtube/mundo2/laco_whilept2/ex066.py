n = 0
q = 0
s = 0

while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    q += 1
    s = s + q
print(f"A todo foi {q}  numeros e a soma foi de: {s}")