print("Digite um número para verificar se é bissexto, digite 0 para saber se o ano atual e bissexto")
ano = int(input("Digite um ano: "))
if ano // 4 == 0 and ano // 100 != 0 or ano // 400 == 0:
    print(f"Esse ano de {ano} é bissexto")
else:
    print(f"Esse ano de {ano} NÃO é bissexto")