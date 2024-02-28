pergunta = int(input("Digite o seu salário: "))
#aum = salario + salario * 15/100
salario = pergunta
aumento =  pergunta * 0.15
salario += aumento
"""Aqui pedia o aumento do salário em 15%. aqui foi o jeito do
Guanabara. mas simplesmente pode ser feito:
salario * 1.15"""

print(f"O seu salário agora vai custar {salario}")