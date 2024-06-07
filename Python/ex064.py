nome = "Josue Silva"
nome_num = len(nome)
print(nome_num)
print(nome[4])

c = 0
while c < nome_num:
    print(f"*{nome[c]}",end="")
    c+=1
print("\nacabou!")
