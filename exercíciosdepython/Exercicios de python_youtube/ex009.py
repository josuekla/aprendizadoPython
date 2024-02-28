numero = int(input("Digite o seu número para a tabuada: "))
print('TABUADA DE SOMA\n')
for n in range(1,11):
    soma = n + numero
    print(f'{numero} + {n} = {soma}')


print('TABUADA DE SUBTRAÇÃO\n')
for n in range(1,11):

    dimi = n - numero
    print(f'{numero} - {n} = {dimi}')

print('TABUADA DE DIVISÃO\n')
for n in range(1,11):

    divi = n / numero
    print(f'{numero} / {n} = {divi}')

print('TABUADA DE MULTIPLICAÇÃO\n')
for n in range(1,11):

    mul = n * numero
    print(f'{numero} x {n} = {mul}')
