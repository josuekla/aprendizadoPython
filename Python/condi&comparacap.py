num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O número1 = {num1} é maior do que o número2 = {num2}")
elif num2 > num1:
    print(f"O número2 = {num2} é maior do que o número1 = {num1}")
elif num2 == num1:
    print(f"O número1 = {num1} e o número2 = {num2} são iguais")
else:
    print("Digite valoresválidos")
