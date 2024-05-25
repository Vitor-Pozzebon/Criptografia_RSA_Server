import os
os.system("cls")

def gerarChaves():
    # FUNÇÃO PARA VERIFICAR SE UM NÚMERO É PRIMO OU NÃO
    # RETORNA 0 : NÃO PRIMO
    # RETORNA 1 : PRIMO
    def primo(n):
        if (n == 1):
            return 1
        for i in range(2, n):
            if ((n % i) == 0):
                return 0
        return 1

    # FUNÇÃO PARA GERAR UM NÚMERO PRIMO
    # RETORNA VETOR COM OS NÚMEROS PRIMOS NO INTERVALO
    def gerarPrimo(inicio, fim):
        aux = []
        for i in range(inicio, fim):
            if (primo(i) == 1):
                aux.append(i)
        return aux

    # Escolher dois numeros primos
    p = 5
    q = 97

    # calculo do quantificador n
    n = p * q

    # Calcular o tociente de Euler
    delta = (p - 1) * (q - 1)

    print("P = ", p)
    print("Q = ", q)
    print("N = ", n)
    print("Delta = ", delta)

    # especifique E   mdc(delta,e)=1 ; 1 < e < delta
    print(gerarPrimo(q + 1, delta))
    print("-" * 60)
    aux = "DIGITE UM NUMERO mdc (" + str(delta) + ",e) = 1 ; 1 < e < " + str(delta) + " : "
    # Chave de criptografia - pública
    E = int(input(aux))

    print("-" * 60)
    print("ESCOLHA DE UM NUMERO PRIMO")
    D = 1
    flag = 100
    while (flag != 1):
        D = D + 1
        flag = (E * D) % delta
        print(E, "*", D, " % ", delta, " FLAG= ", flag)
        if (flag == 1):
            print("-" * 60)
            print("CHAVE PÚBLICA: [", E, ",", n, "]")
            print("CHAVE PRIVADA: [", D, ",", n, "]")
            print("-" * 60)

    chavePublica = [E, n]
    chavePrivada = [D, n]

    return [chavePublica, chavePrivada]