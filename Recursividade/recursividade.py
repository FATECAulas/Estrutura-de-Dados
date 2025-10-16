#DIVISÃO RECURSIVA
def divide (a, b):
    if a < b:
        return 0
    else:
        return 1 + divide (a - b, b)

def main():
    print("Forneça valores para a e b:")

    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))

    resultado = divide(a, b)
    print(f"Resultado = {resultado}")

if __name__ == "__main__":
    main()



#MULTIPLICAÇÃO RECURSIVA
def multiplica(a, b):
    if b == 0:
        return b
    elif b == 1:
        return a
    else:
        return a + multiplica (a, b - 1)

def main():
    print("Forneça valores para a e b:")

    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))

    resultado = multiplica(a, b)
    print(f"Resultado = {resultado}")

if __name__ == "__main__":
    main()



#INVERTE LINHA DE TEXTO
def exibe_invertido(mensagem, tamanho):
    if tamanho >= 0:
        print(mensagem [tamanho], end=" ")
        exibe_invertido(mensagem, tamanho -1)
    
def main():
    print("Forneça a mensagem:")

    mensagem = input("Digite a mensagem: ")
    tamanho = len(mensagem) - 1

    print("Mensagem invertida:")
    exibe_invertido(mensagem, tamanho)
    print()

if __name__ == "__main__":
    main()   



#SOMA DE ELEMENTOS DE UM VETOR
def soma_elementos(V, N):
    if N == 0:
        return V[N]
    else:
        return V[N] + soma_elementos(V, N - 1)

def main():
    N = int(input("Quantidade de números: "))
    print("Entre com os números: ")
    V = []
    for i in range(N):
        numero = int(input(f"Número {i + 1}: "))
        V.append(numero)
    
    resultado = soma_elementos(V, N - 1)

    print(f"Resultado = {resultado}")

if __name__ == "__main__":
    main()



#MAIOR ELEMENTO DE UM VETOR
def maximo(elemento1, elemento2):
    if elemento1 > elemento2:
        return elemento1
    else:
        return elemento2
    
def max_array(array, a, b):
    if a == b:
        return array[a]
    else:
        mid = (a + b) // 2
        x = maximo(max_array(array, a, mid), max_array(array, mid + 1, b))
    return x

def main():
    N = int(input("Entre com a quantidade de números: "))

    V = []
    print("Entre com os números: ")
    for i in range(N):
        numero = int(input(f"Número {i + 1}: "))
        V.append(numero)
    
    inicio = 0
    fim = N - 1

    resultado = max_array(V, inicio, fim)

    print(f"Resultado = {resultado}")

    if __name__ == "__main__":
        main()