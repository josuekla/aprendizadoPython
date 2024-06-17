while True:
    cpf = input("Digite o seu cpf: ")

    cpf_valido =False
    numeros_cpf = []

    try:
        soma = 0
        if "-" in cpf and "." in cpf:
            cpf = "".join(cpf.split("-")).replace(".","")
            print(cpf)
        if len(cpf) == 11:
            cpf_valido = True
        else:
            print("Valor inválido ")
        for digito in cpf:
            numeros_cpf.append(int(digito))
        # Removendo os dois últimos números do CPF
        dois_ultimos_num_removidos = numeros_cpf[0:9]
        for numeros in range(10,1,-1):
            soma += (numeros_cpf[10 - numeros] * numeros)




    except ValueError:
        print("Digite apenas números")

