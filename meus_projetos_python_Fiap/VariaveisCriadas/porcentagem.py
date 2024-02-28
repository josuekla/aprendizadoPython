'''importando sys'''
import sys
print(sys.path)

def calcular_porcentagem(valor, percentual):
    '''Este é uma funcão que calcula a porcentagem,o primeiro e o valor e segundo e porcentagem,'''
    if not 0 <= percentual <= 100:
        raise ValueError("O percentual deve estar entre 0 e 100.")

    resultado = valor * (percentual / 100)

    return resultado
