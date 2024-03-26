from socket import *
servidor = "127.0.0.1"
porta = 43210
objSocket = socket(AF_INET,SOCK_STREAM)
objSocket.bind((servidor,porta))
objSocket.listen(2)
print("Aguardando o cliente ...")
while True:
    con, cliente = objSocket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", str(msg_recebida)[2:-1])
        msg_enviada = bytes(input("Digite algo: "), "utf-8")
        con.send(msg_enviada)
        break
    con.close()