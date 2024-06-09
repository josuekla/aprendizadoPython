import os


print("\033[34m" + "Vamos jogar o Jogo da palavra secreta".center(50, "-")+ "\033[0m")
# print("Dica: Profissão")



palavra_secreta = "odisseia"
letras_corretas = ''
loser = 0
tentativas = 0
while True:
    
    palavra_usuario = input("\033[33m"+"Digite apenas uma letra para adivinhar a palavra: ").lower()
    numD = len(palavra_usuario)


    try:
        if numD > 1 :
            print("\033[31m"+"Você digitou mais deu uma letra ou \ndigitou número\n.")
        float(palavra_usuario)
        print("Você tentou digitar um número")
        continue
    
    except:


        # if numD == 1:
            # validar = True
        palavra_formada = ""
        if palavra_usuario in palavra_secreta:
            letras_corretas += palavra_usuario

        for letras_secretas in palavra_secreta:
            if letras_secretas in letras_corretas:
                palavra_formada += letras_secretas
            else:
                palavra_formada += "*"

        loser += 1
        if palavra_usuario not in palavra_secreta:
            tentativas += 1
            print(f"Você errou {tentativas} vezes")
        if tentativas == 5:
            print("\033[31m" + "VOCÊ JÁ ERROU 5 VEZES")
            print("A palavra era", palavra_secreta)
            break
        print("Palavra formada: ", palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print("PARABÉNS VOCÊ GANHOU!!!")
            print("A palavra era", palavra_secreta)
            print("Tentativas:", loser, "vezes")
            letras_corretas = ""
            loser = 0   
            




            # indentacao = palavra_secreta.index(palavra_usuario)
            # print(f"A palavra achada foi: \"{palavra_secreta[indentacao]}\"")
            # for contador in palavra_secreta:
            #     if contador != palavra_usuario:
            #         print("*", end="")
                
            #     if contador == palavra_usuario:
            #         print(palavra_usuario, end="")

            

        # elif palavra_usuario not in palavra_secreta:
        #     print("Sua palavra é","*"*len(palavra_secreta))
            
    # else:
            

    

        




    #     sair = input("Deseja sair?").lower().startswith("s")

    #     if sair is True:


    #         break