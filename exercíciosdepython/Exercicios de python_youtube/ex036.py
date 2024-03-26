valorCasa = float(input("Digite o valor da sua casa: "))
salario = float(input("Digite o seu salário: "))
porcentagem = salario * 0.3
print(porcentagem)
anos = int(input("Anos de financiamento: "))
meses = anos * 12
print(meses)
total_pagar = valorCasa / meses

if total_pagar > porcentagem:
    print(f"O valor da casa será de {valorCasa:.2f}, e você pagará em {anos} anos, \n"
            f"e sua prestação será de {total_pagar:.2f}. Empréstimo não aprovado")
elif total_pagar <= porcentagem:
    print(f"O valor da casa será de {valorCasa:.2f}, e você pagará em {anos}, \n"
            f"e sua prestação será de {total_pagar:.2f}. Empréstimo aprovado")
