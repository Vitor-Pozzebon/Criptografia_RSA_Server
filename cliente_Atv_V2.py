import socket
import os

os.system("cls")

chavePublica = [193,485]

def criptografar(texto, chave):
    #Chave pública
    E = chave[0]
    n = chave[1]
    cripto = ""
    for i in texto:
        # Conversão para o valor ASCII
        vl = ord(i)
        print("CARACTER: ", i, " ASCII: ", vl)
        cp = (vl ** E) % n
        strcp = str(cp).zfill(3)
        print("ASCII: ", vl, " RSA: ", strcp)
        print("-" * 30)
        cripto = cripto + strcp
        print("MENSAGEM CRIPTOGRAFADA: ", cripto)
        print("-" * 60)
    return cripto

# PRGRAMA PRINCIPAL

while (True):
    print("-" * 60)
    msgFromClient = input("DIGITE UMA MENSAGEM PARA SER ARMAZENADA: ")

    # CRIPTOGRAFAR A MENSAGEM
    criptografada = criptografar(msgFromClient, chavePublica)

    bytesToSend         = str.encode(criptografada)
    serverAddressPort   = ("192.168.100.37", 20001)
    bufferSize          = 1024

    # DEFINIR UM SOCKET UDP PARA O CLIENTE
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # ENVIAR MENSAGEM PARA SERVIDOR UTILIZANDO O SOCKET UDP ATIVADO
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "MENSAGEM DO SERVIDOR {}".format(msgFromServer[0])
    print(msg)
    print("-" * 60)