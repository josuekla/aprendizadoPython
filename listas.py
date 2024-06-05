# a = [1, 2]
# b = [3, 6]

# c = a + b
# d = a * 3
# print(c)
# print(d)
lista = [1,4,5,6,8,3]


lista.sort()  # Ordena em ordem crescente
lista.sort(reverse=True)  # Ordena em ordem decrescente
lista.reverse()  # Inverte a lista

print(lista)
# Iterando sobre a lista
for elemento in lista:
    print(elemento)

# Iterando com índices
for indice, valor in enumerate(lista):
    print(f"{indice}: {valor}")


