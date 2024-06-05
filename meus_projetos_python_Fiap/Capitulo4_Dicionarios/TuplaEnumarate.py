usuarios = {}
emails = []
resp = "S"
while resp == "S":
    emails.append(input("Digite o seu email: ").lower())
    resp = input("Digite <S> para cotinuar: ").upper()


tupla = list(enumerate(emails))  # enumerando cada email gerando uma tupla em cada elemento(funcao: list())
for chave in range(0, len(tupla)):  # laço atrelado em nossa tupla,ou seja, a quantidade de emails que foram armazenado
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome:"), [input("Digite o nível: ")]]

for chave, dado in usuarios.items():
    print("Usuário.:", chave[0])
    print("email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])
