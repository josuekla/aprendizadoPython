frase = input("Digite uma frase: ").upper() #ana maria da silva
semEspaco = frase.strip()
frase_01 = frase.replace(" ","") #anamariadasilva
print("A letra A aparece {} vezes na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A última letra A apareceu na posição {}".format(frase_01.rfind("A")+1))
