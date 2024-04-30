from random import randint


print("\nVAMOS JOGAR PAR OU IMPAR")
print("SE GANHAR JOGA NOVAMENTE!\n")

esc = 'PI'
while True:
    rpc = randint(1, 10)
    esc = input("Escolha par ou ímpa: [P/I] ").upper()
    num = int(input("diga um número: "))
    soma = rpc + num

    if esc == "P":
        if (rpc + num) % 2 == 0:
            print("Parabéns vc ganhouu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}\n")

        elif (rpc + num) % 2 != 0:
            print("Você perdeu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}")
            break

    elif esc == "I":
        if (rpc + num) % 2 != 0:
            print("Parabéns vc ganhouu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}\n")

        elif (rpc + num) % 2 == 0:
            print("Você perdeu!")
            print(f"COM escolheu o número {rpc} e você {num} dando o resultado {soma}")
            break
    else:
        break





