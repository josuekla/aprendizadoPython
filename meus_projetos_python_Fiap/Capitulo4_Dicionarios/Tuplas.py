ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primerios octetos:  "), input("Digite os dois últimos octetos: "))] = input(
        "Nome da máquina: "
    )
    resp = input("Digite <S> para continua").upper()

print("Exibindo os ip´s: ")
for ip in ips.keys():
    print(ip[0], ".", ip[1])

print("Exibindo as máquinas com o mesmo endereço:  ")

pesquisa = input("Digite os dois últimos octetos: ")
print("Exibindo as máquinas com mesmo ip: ")
for ip, nome in ips.items():
    if ip[1] == pesquisa:
        print(nome)
print("Exibindo as máquinas que compõem uma mesma rede:")
rede = input("Digite os dois primeiros octetos:")
for ip, nome in ips.items():
    if ip[0] == rede:
        print(nome)

