with open("teste.txt", "w") as arquivo:  # Recomendado utilizr o combinado open() + with
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "a") as arquivo:
    arquivo.write("Continuação do texto.")