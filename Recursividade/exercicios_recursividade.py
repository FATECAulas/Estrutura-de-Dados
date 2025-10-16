# Desenvolva uma função recursiva que calcule o resto da 
# divisão inteira de A por B (A % B), também utilizando 
# subtrações sucessivas.
# Exemplo: MOD(18, 4) deve retornar 2.
def mod(a, b):
    if a < b:
        return a
    else:
        return mod(a - b, b)

def main():
    print("Forneça valores para a e b:")

    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))

    resultado = mod(a, b)
    print(f"Resto = {resultado}")

if __name__ == "__main__":
    main()



# Crie uma função recursiva que determine se um número inteiro 
# A é múltiplo de outro número inteiro B.
# Exemplo: is_multiple(16, 4) deve retornar True; 
# is_multiple(17, 4) deve retornar False.
def is_multiple(a, b):
    if a < b:
        return False
    elif a == b:
        return True
    else:
        return is_multiple(a - b, b)

def main():
    print("Verificador de múltiplos")

    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    if is_multiple(a, b):
        print(f"{a} é múltiplo de {b}")
    else:
        print(f"{a} não é múltiplo de {b}")

if __name__ == "__main__":
    main()



# Escreva uma função recursiva para calcular A elevado à potência B 
# (A^B) utilizando multiplicações sucessivas.
# Exemplo: POWER(2, 3) deve retornar 8.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

def main():
    print("Cálculo de potência recursiva")

    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    resultado = power(a, b)
    print(f"Resultado = {resultado}")

if __name__ == "__main__":
    main()



# Crie uma função recursiva que determine se uma determinada string 
# é um palíndromo.
# Exemplo: is_palindrome("arara") deve retornar True; 
# is_palindrome("hello") deve retornar False.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

def main():
    palavra = input("Digite uma palavra: ")

    if is_palindrome(palavra):
        print(f'"{palavra}" é um palíndromo!')
    else:
        print(f'"{palavra}" não é um palíndromo!')

if __name__ == "__main__":
    main()



# De forma semelhante ao exercício anterior, implemente uma função 
# recursiva que encontre o menor elemento em um vetor de números 
# inteiros.
# Exemplo: Para V=[11, 2, 3, 14, 15], o menor elemento deve ser 2.
def menor_elemento(V, N):
    if N == 0:
        return V[0]
    else:
        menor_restante = menor_elemento(V, N - 1)
        if V[N] < menor_restante:
            return V[N]
        else:
            return menor_restante

def main():
    N = int(input("Quantidade de números: "))
    print("Entre com os números: ")
    V = []
    for i in range(N):
        numero = int(input(f"Número {i + 1}: "))
        V.append(numero)
    
    resultado = menor_elemento(V, N - 1)
    print(f"Menor elemento = {resultado}")

if __name__ == "__main__":
    main()



# Crie uma função recursiva para calcular o fatorial de um número 
# inteiro não negativo N.
# Exemplo: factorial(5) deve retornar 120.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = int(input("Digite um número inteiro não negativo: "))
    if n < 0:
        print("Número inválido! Digite um inteiro não negativo.")
    else:
        resultado = factorial(n)
        print(f"{n}! = {resultado}")

if __name__ == "__main__":
    main()



# Implemente uma função recursiva que retorne o N-ésimo termo da 
# sequência de Fibonacci.
# Exemplo: fibonacci(6) deve retornar 8.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Digite o valor de N: "))
    if n < 0:
        print("Número inválido! Digite um inteiro não negativo.")
    else:
        resultado = fibonacci(n)
        print(f"O {n}-ésimo termo da sequência de Fibonacci é {resultado}")

if __name__ == "__main__":
    main()



# Desenvolva uma função recursiva para calcular o 
# Máximo Divisor Comum (MDC) de dois números inteiros A e B, 
# utilizando o algoritmo de Euclides.
# Exemplo: gcd(48, 18) deve retornar 6.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    resultado = gcd(a, b)
    print(f"O MDC de {a} e {b} é {resultado}")

if __name__ == "__main__":
    main()



# Escreva uma função recursiva que calcule a soma dos dígitos 
# de um número inteiro positivo.
# Exemplo: sum_digits(123) deve retornar 6.
def sum_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_digits(n // 10)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Número inválido! Digite um inteiro positivo.")
    else:
        resultado = sum_digits(n)
        print(f"A soma dos dígitos de {n} é {resultado}")

if __name__ == "__main__":
    main()



# Crie uma função recursiva para contar quantos dígitos tem um 
# número inteiro positivo.
# Exemplo: count_digits(12345) deve retornar 5.
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Número inválido! Digite um inteiro positivo.")
    else:
        resultado = count_digits(n)
        print(f"O número {n} tem {resultado} dígitos.")

if __name__ == "__main__":
    main()



# Implemente uma função recursiva que conte o número de vezes que 
# um determinado caractere aparece em uma string.
# Exemplo: count_char("banana", 'a') deve retornar 3.
def count_char(s, c):
    if s == "":
        return 0
    else:
        if s[0] == c:
            return 1 + count_char(s[1:], c)
        else:
            return count_char(s[1:], c)

def main():
    texto = input("Digite uma string: ")
    caractere = input("Digite o caractere a contar: ")

    if len(caractere) != 1:
        print("Por favor, digite apenas um caractere.")
    else:
        resultado = count_char(texto, caractere)
        print(f'O caractere "{caractere}" aparece {resultado} vezes na string.')

if __name__ == "__main__":
    main()



# Desenvolva uma função recursiva para realizar uma busca binária 
# em um vetor de números inteiros ordenado, procurando por um 
# elemento específico.
# Exemplo: Para V=[2, 5, 8, 12, 16, 23, 38, 56, 72, 91] 
# e buscando 23, deve retornar o índice 5.
def busca_binaria(V, x, inicio, fim):
    if inicio > fim:
        return -1  
    meio = (inicio + fim) // 2
    if V[meio] == x:
        return meio
    elif V[meio] < x:
        return busca_binaria(V, x, meio + 1, fim)
    else:
        return busca_binaria(V, x, inicio, meio - 1)

def main():
    V = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    x = int(input("Digite o elemento a buscar: "))
    
    resultado = busca_binaria(V, x, 0, len(V) - 1)
    
    if resultado != -1:
        print(f"Elemento {x} encontrado no índice {resultado}.")
    else:
        print(f"Elemento {x} não encontrado no vetor.")

if __name__ == "__main__":
    main()



# Crie uma função recursiva que determine se um vetor de números 
# inteiros está ordenado de forma crescente.
# Exemplo: is_sorted([1, 2, 3, 4, 5]) deve retornar True; 
# is_sorted([1, 3, 2, 4]) deve retornar False.
def is_sorted(V):
    if len(V) <= 1:
        return True
    if V[0] <= V[1]:
        return is_sorted(V[1:])
    else:
        return False

def main():
    V = list(map(int, input("Digite os números do vetor separados por espaço: ").split()))
    
    if is_sorted(V):
        print("O vetor está ordenado de forma crescente.")
    else:
        print("O vetor NÃO está ordenado de forma crescente.")

if __name__ == "__main__":
    main()



# Simule o clássico problema da Torre de Hanói para N discos. 
# A função recursiva deve imprimir os passos necessários para mover 
# os discos.
# Exemplo: Para N=3, a função deve imprimir os passos.
def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        hanoi(n-1, origem, auxiliar, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        hanoi(n-1, auxiliar, destino, origem)

def main():
    n = int(input("Digite o número de discos: "))
    print(f"Passos para mover {n} discos da Torre de Hanói:")
    hanoi(n, "A", "C", "B") 

if __name__ == "__main__":
    main()