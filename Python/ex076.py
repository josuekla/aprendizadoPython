print("Vamos jogar o Jogo da palavra secreta".center(50, "-"))
palavra_secreta = "LEALDADE"
letras_corretas = ''
while True:

    palavra_usuario = input("Digite apenas uma letra para adivinhar a palavra: ").upper()
    numD = len(palavra_usuario)


    try:
        if numD > 1 :
            print("Você digitou mais deu uma letra ou \ndigitou número\n.")
        float(palavra_usuario)
        print("Você tentou digitar um número")
        continue
    
    except:

      

        loser = 0
        # if numD == 1:
            # validar = True
                
        if palavra_usuario in palavra_secreta:
            letras_corretas += palavra_usuario

        for letras_secretas in palavra_secreta:
            if letras_secretas in letras_corretas:
                print(letras_secretas)
            else:
                print("*")


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