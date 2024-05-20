contador = 0

while True:
    for c in range(1,5):
        n = float(input(f"Digite o {c} número:"))
        resp = input("DESEJA CONTINUAR? [S/N]").upper()
        contador += 1
        soma += n 
        if resp != "S":
            break
