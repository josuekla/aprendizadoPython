from random import randint
vitoria = 0
derrota = 0


print("\nVAMOS JOGAR PAR OU IMPAR")
print("SE GANHAR JOGA NOVAMENTE!\n")

resp = 'S'
while resp == 'S':
    rpc = randint(1, 10)
    esc = input("Escolha par ou ímpa: [P/I] ").upper()
    
    num = int(input("diga um número: "))
    soma = rpc + num

    if esc == "P":
        if (rpc + num) % 2 == 0:
            print("Parabéns vc ganhouu!")
            print(f"Deu PAR, COM escolheu o número {rpc} e você {num} dando o resultado {soma}\n")
            vitoria += 1

        elif (rpc + num) % 2 != 0:
            print("Você perdeu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}")
            derrota += 1
            break

    elif esc == "I":
        if (rpc + num) % 2 != 0:
            print("Parabéns vc ganhouu!")
            print(f"Deu IMPA,COM escolheu o número {rpc} e você {num} dando o resultado {soma}\n")
            vitoria += 1

        elif (rpc + num) % 2 == 0:
            print("Você perdeu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}")
            derrota += 1
            break
    else:
        break
ver = input("\nDeseja ver quantas ganhou e perdeu? [S/N]").upper()
if ver == 'S':
    print(f"Você ganhou {vitoria} vezes \n"
    f"perdeu {derrota}.")




