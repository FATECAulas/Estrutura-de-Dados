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
def inverte():
    if