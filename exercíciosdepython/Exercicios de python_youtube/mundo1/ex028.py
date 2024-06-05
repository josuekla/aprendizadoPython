from random import randint
import time
numero = int(input("Digite um número de 0 a 5: "))
print("Escolhendo um número")
print("PROCESSANDO...")
time.sleep(2)
escolhido = randint(0,5)
if numero == escolhido:
    print("PARABÉNS! Você acertou!")
else:
    print(f"O número escolhido foi {escolhido}, e o seu número foi {numero}")