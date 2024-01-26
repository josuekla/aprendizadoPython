for numero in range(1,int(input("Digite um número para determinar o fim: ")),1):
    print("            ",str(numero))
    

#FOR criou uma variavel "numero" e de acordo com a função
# "range()" ---> Que permite especificar uma faixa de valores e como será incrementada
# comecará do 1 até atingir o númeroo desejado


#input("Digite um numero para determinar o fim: "): Este comando solicita ao usuário que insira um número. A mensagem "Digite um numero para determinar o fim: " é exibida para o usuário para indicar o que ele deve fazer.

#int(...): Este comando converte a entrada do usuário em um número inteiro. Isso é necessário porque a função input() retorna uma string por padrão.

#range(1, ..., 1): A função range() gera uma sequência de números começando pelo primeiro argumento (neste caso, 1), até o segundo argumento (o número inserido pelo usuário), incrementando de um em um (terceiro argumento).

#for numero in ...: Este é um loop for que itera sobre a sequência de números gerada pela função range(). Em cada iteração, o valor atual é atribuído à variável numero.

#print ("	" + str(numero)): Dentro do loop, este comando imprime o valor atual de numero, precedido por uma tabulação. A função str() é usada para converter o número em uma 

