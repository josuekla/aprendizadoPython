tabuada= int(input('Digite o número para a tabuada: '))
print('O número será:', tabuada)
for numero in range(1,11,1):
    print(f'O resultado será: {tabuada} x {numero} = {tabuada*numero}')