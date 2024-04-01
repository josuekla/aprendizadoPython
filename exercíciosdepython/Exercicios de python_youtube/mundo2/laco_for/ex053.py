frase = str(input("Digite a frase PALINDROMA: ")).upper().split()
junto = "".join(frase)
oposto = junto[::-1]
print(junto)
print(oposto)
print(f"A frase {junto} invertida fica {oposto}")

if junto == oposto:
    print("Essa frase é uma PALINDROMA")
else:
    print("Essa frase não é uma PALINDROMA")