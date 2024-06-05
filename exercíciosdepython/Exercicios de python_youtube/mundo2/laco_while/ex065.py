n = 0
quant = 0
soma = 0
resp = "S"
maior = 0
menor = 0
while resp == "S":
    n = int(input("Digite um valor: "))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n



    resp = input("Digite <S> para contunuar: ").upper()

media = soma/quant
print(f"Ao todo foi {quant} números, sendo o maior {maior}, e o menor {menor}")