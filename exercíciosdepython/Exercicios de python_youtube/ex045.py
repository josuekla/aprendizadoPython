from time import sleep
from random import randint
escolhacom = randint(0,3)


print("""Escolha uma opção para jogar:
< 1 > Pedra
< 2 > Tesoura
< 3 > Papel""")
opcaoJog = int(input("Sua opção: "))

print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA\n")

if opcaoJog == 1 and escolhacom == 2:
    print("JOGADOR VENCE, o COM escolheu TESOURA")

elif opcaoJog == 1 and escolhacom == 3:
    print(f"Perdeu, o COM escolheu PAPEL")

elif opcaoJog == 2 and escolhacom == 1:
    print(f"Perdeu, o COM escolheu PEDRA")

elif opcaoJog == 2 and escolhacom == 3:
    print("JOGADOR VENCE, o COM escolheu PAPEL")

elif opcaoJog == 3 and escolhacom == 2:
    print(f"Perdeu, o COM escolheu TESOURA")

elif opcaoJog == 3 and escolhacom == 1:
    print(f"JOGADOR VENCE, o Com Esconlheu Pedra")

else:
    print("EMPATE")
