while True:
    numero1 = input("Digite o Primeiro valor: ")
    numero2 = input("Digite o Segundo valor: ")
    operador = input("Escolha o operador(+-*/): ")

    numero_valido = None



    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_valido = True
        ##########################
        
        
        
        ##########################

        if operador == "+": 
            soma = numero1_float + numero2_float
            print(f"A soma de {numero1_float} com {numero2_float} = {soma}")

        elif operador == "-": 
            subtração = numero1_float - numero2_float
            print(f"A subtração de {numero1_float} com {numero2_float} = {subtração}")

        elif operador == "*":
            multiplicação = numero1_float * numero2_float
            print(f"A multiplicação de {numero1_float} com {numero2_float} = {multiplicação}")

        elif operador == "/":
            divisao = numero1_float / numero2_float
            print(f"A divisão de {numero1_float} com {numero2_float} = {divisao}")


    except:
        numero_valido = None
            
    if numero_valido is None:
        print("Algum valor digitado é inválido")
        continue
                
    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        print("Digite operador válidos")
        continue
            
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
        
        
        
        
    sair = input("Deseja Sair?").lower().startswith("s")
    if sair is True:
            break



















# num = int(input("Digite um valor para a tabuada: "))
# contador = 1
# mul = "Tabuada de Multiplicação"


# print(f'{mul:^}')
# while contador <=10:
#     resultado = num * contador  
#     print(f"{num:2} X {contador:2} = {resultado:2}")
#     contador += 1
# print("Acabou!")