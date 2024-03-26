from socket import *

servidor = "127.0.0.1"
porta = 43210

while True:
    objSocket = socket(AF_INET,SOCK_STREAM)
    objSocket.connect((servidor,porta))
    msg = bytes(input('Digite algo: '), "utf-8")
    objSocket.send(msg)
    resposta = objSocket.recv(1024)
    print("Recebemos: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper() == "FIM":
        break
objSocket.close()
