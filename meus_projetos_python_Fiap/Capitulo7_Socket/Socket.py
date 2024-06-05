import socket
resp = "S"
while resp == "S":
    url = input('Digite uma url: (ex: www.google.com:) ')
    ip = socket.gethostbyname(url)
    print('O IP da url é:', ip)
    print(socket.getservbyname("domain"))
    print(socket.getservbyname("http"))
    print(socket.getservbyname("ftp"))

    resp = input('Digite S para continuar: ').upper()



