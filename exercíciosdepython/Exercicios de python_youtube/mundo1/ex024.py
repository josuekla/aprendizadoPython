# Aqui nesse exercício, deveria ser verdadeiro somente se a palavra SANTO tivesse na frase do usuário
city = "SANTO"
nome_cidade = input("Digite a sua cidade: ").upper()
resultado = city in nome_cidade
print(resultado)