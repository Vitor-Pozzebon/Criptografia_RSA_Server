import socket
import os
import gerarChaves as gc

os.system("cls")

host = socket.gethostname()
localIP = socket.gethostbyname(host)

print("IP LOCAL: ", localIP)
print("-" * 60)

localPort   = 20001
bufferSize  = 1024

chavePrivada = gc.gerarChaves()[1]

def decriptografar(cripto, chave):
    #Chave privada
    D = chave[0]
    n = chave[1]
    decripto = ""
    for vl in range(0, len(cripto), 3):
        ftoken = cripto[vl:vl+3]
        vl = int(ftoken)
        dcp = (vl ** D) % n
        print("BLOCO RSA: ", ftoken, " ASCII: ", dcp)
        caracter = chr(dcp)
        print("ASCII: ", dcp, " CARACTER: ", caracter)
        decripto = decripto + caracter
        print("-" * 30)
        print("MENSAGEM DECRIPTOGRAFADA: ", decripto)
        print("-" * 60)

    # Armazenar a frase no arquivo de frases originais
    f = open('arquivoOriginais.txt', 'a', encoding="utf-8")
    f.write(decripto + "\n")
    f.close()
    print("-" * 60)
    print("MENSAGEM ORIGINAL ARMAZENADA COM SUCESSO!")
    print("-" * 60)

    return decripto

msgFromServer= "MENSAGEM RECEBIDA PELO SERVIDOR ...."
bytesToSend= str.encode(msgFromServer)

# CRIAR UM datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# DEFINIR VÍNCULOS ENTRE O ENDEREÇO E O IP
UDPServerSocket.bind((localIP, localPort))

print("-" * 60)
print("UDP - SERVIDOR ATIVADO E ESPERANDO MENSAGEM")
print("-" * 60)
print("-" * 60)

# ESPERANDO POR MENSAGEM
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode()

    address = bytesAddressPair[1]

    clientMsg = "MENSAGEM DO CLIENTE: {}".format(message)
    clientIP  = "IP DO CLIENTE Address:{}".format(address)
    
    print("-" * 60)
    print(clientMsg)
    print(clientIP)

    # GRAVAR EM ARQUIVO - Frases criptografadas
    f = open('arquivoCriptografadas.txt', 'a', encoding="utf-8")
    f.write(message + "\n")
    f.close()
    print("-" * 60)
    print(message, ": MENSAGEM CRIPTOGRAFADA ARMAZENADA COM SUCESSO!")
    print("-" * 60)

    # FUNÇÃO PARA REALIZAR A DECRIPTOGRAFIA
    decriptografar(message, chavePrivada)

    # MENSAGEN DE RESPOSTA AO CLIENTE
    UDPServerSocket.sendto(bytesToSend, address)