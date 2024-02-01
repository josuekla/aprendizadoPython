ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primerios octetos:  "), input("Digite os dois últimos octetos: "))] = input(
        "Nome da máquina: "
    )
    resp = input("Digite <S> para continuar: ")

