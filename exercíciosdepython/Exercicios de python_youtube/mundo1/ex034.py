salario = float(input("Digite o seu sário: "))
if salario <= 1250:
    custo = salario + (salario * 0.15)
    print(f"O seu aumento foi de: {custo}")
else:
    custo = salario + (salario * 0.10)
    print(f"O seu salário foi de: {custo}")