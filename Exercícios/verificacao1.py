# 1. Implemente o algoritmo Bubble Sort para ordenar uma lista 
# de números inteiros em ordem crescente.
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        print(f'Iteraçãp{i+1}:{lista}') #OPCIONAL
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(f'Resultado final: {lista}')
    return lista

numeros = [2, -5, 7, 90, 1]
bubble_sort(numeros)



# 2. Crie uma função que utilize Selection Sort para ordenar uma lista 
# de strings em ordem alfabética.
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista 

lista = ["K", "J", "A", "C", "D", "O"]
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)



# 3. Desenvolva o algoritmo Insertion Sort para ordenar uma lista 
# de números decimais.
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

lista = [1.2, -1.2, 3.7, 7.04]
insertion_sort(lista)
print(lista) 



# 4. Implemente o Merge Sort de forma recursiva para ordenar uma lista 
# de números inteiros.
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

numeros = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(numeros))



# 5. Crie uma função Quick Sort que ordene uma lista de números 
# e retorne o número de comparações realizadas.
def quick_sort(lista):
    comparacoes = [0]  

    def _quick_sort(lista, inicio, fim):
        if inicio < fim:
            p = particiona(lista, inicio, fim)
            _quick_sort(lista, inicio, p - 1)
            _quick_sort(lista, p + 1, fim)

    def particiona(lista, inicio, fim):
        pivo = lista[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            comparacoes[0] += 1  
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        return i + 1

    _quick_sort(lista, 0, len(lista) - 1)
    return lista, comparacoes[0]

numeros = [38, 27, 43, 3, 9, 82, 10]
ordenado, comps = quick_sort(numeros)
print("Quick Sort:", ordenado)
print("Comparações realizadas:", comps)



# 6. Modifique o Bubble Sort para ordenar uma lista em ordem decrescente 
# e conte o número de trocas realizadas.
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        print(f'Iteraçãp{i+1}:{lista}') 
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(f'Resultado final: {lista}')
    return lista

numeros = [2, -5, 7, 90, 1]
bubble_sort(numeros)



# 7. Implemente o Selection Sort que encontre tanto o 
# menor quanto o maior elemento em cada iteração.
def selection_sort_min_max(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        # Assume que o primeiro é o menor e o maior
        min_index = inicio
        max_index = inicio

        for i in range(inicio, fim + 1):
            if lista[i] < lista[min_index]:
                min_index = i
            elif lista[i] > lista[max_index]:
                max_index = i

        # Troca o menor com o início
        lista[inicio], lista[min_index] = lista[min_index], lista[inicio]

        # Ajusta se o maior foi trocado junto
        if max_index == inicio:
            max_index = min_index

        # Troca o maior com o fim
        lista[fim], lista[max_index] = lista[max_index], lista[fim]

        inicio += 1
        fim -= 1

    return lista

numeros = [29, 10, 14, 37, 14, 5, 98, 1]
print("Selection Sort Min-Max:", selection_sort_min_max(numeros))



# 8. Crie uma versão do Insertion Sort que ordene três listas 
# pelo segundo elemento de cada lista.
def insertion_sort_segundo(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Comparação feita pelo segundo elemento
        while j >= 0 and lista[j][1] > chave[1]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

    return lista

listas = [[1, 9], [2, 3], [3, 7], [4, 1], [5, 5]]
print("Insertion Sort pelo segundo elemento:", insertion_sort_segundo(listas))



# 9. Desenvolva uma comparação de tempo de execução entre 
# Bubble Sort e Quick Sort para uma lista de 1000 elementos.
import random
import time

# ---------- Bubble Sort ----------
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# ---------- Quick Sort ----------
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)


# ---------- Teste de tempo ----------
lista_original = [random.randint(1, 10000) for _ in range(1000)]

# Bubble Sort
lista1 = lista_original.copy()
inicio = time.time()
bubble_sort(lista1)
fim = time.time()
print("Tempo Bubble Sort:", fim - inicio, "segundos")

# Quick Sort
lista2 = lista_original.copy()
inicio = time.time()
quick_sort(lista2)
fim = time.time()
print("Tempo Quick Sort:", fim - inicio, "segundos")



# 10. Implemente o Merge Sort iterativo para ordenar uma lista de números.
def merge_sort_iterativo(lista):
    largura = 1
    n = len(lista)

    def merge(esq, dir):
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1
        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado

    while largura < n:
        for i in range(0, n, 2 * largura):
            lista[i:i + 2 * largura] = merge(lista[i:i + largura], lista[i + largura:i + 2 * largura])
        largura *= 2
    return lista

numeros = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort Iterativo:", merge_sort_iterativo(numeros))



# 11. Crie uma função que remova todos os elementos duplicados de uma lista 
# mantendo a ordem original dos elementos.
def remover_duplicados(lista):
    vistos = set()
    resultado = []
    for item in lista:
        if item not in vistos:
            resultado.append(item)
            vistos.add(item)
    return resultado

numeros = [1, 2, 3, 2, 4, 1, 5, 3]
print("Sem duplicados:", remover_duplicados(numeros))



# 12. Desenvolva uma função que encontre o segundo maior elemento em uma lista 
# sem usar funções de ordenação.
def segundo_maior(lista):
    if len(lista) < 2:
        return None  
    
    maior = segundo = float('-inf')
    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif maior > num > segundo:
            segundo = num
    return segundo if segundo != float('-inf') else None

numeros = [10, 20, 4, 45, 99, 99]
print("Segundo maior:", segundo_maior(numeros))



# 13. Implemente uma função que inverta uma lista.
def inverter_lista(lista):
    return lista[::-1] 

numeros = [1, 2, 3, 4, 5]
print("Lista invertida:", inverter_lista(numeros))



# 14. Crie uma função que mescle duas listas ordenadas em uma única lista ordenada.
def mesclar_listas(lista1, lista2):
    i = j = 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]
print("Listas mescladas:", mesclar_listas(a, b))



# 15. Implemente uma classe Pilha com os métodos push, pop, e is_Empty.
class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        return None  

    def is_empty(self):
        return len(self.itens) == 0

p = Pilha()
p.push(10)
p.push(20)
p.push(30)
print("Pop:", p.pop())  
print("Está vazia?", p.is_empty())  



# 16. Use uma pilha para verificar se uma expressão com parênteses está balanceada.
def expressao_balanceada(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expressao:
        if char in "([{":
            pilha.append(char)
        elif char in ")]}":
            if not pilha or pilha[-1] != pares[char]:
                return False
            pilha.pop()

    return len(pilha) == 0

print(expressao_balanceada("(a+b) * (c-d)"))   
print(expressao_balanceada("(a+b]"))           



# 17. Crie uma função que converta um número decimal para binário usando uma pilha.
def decimal_para_binario(numero):
    pilha = []

    if numero == 0:
        return "0"

    while numero > 0:
        pilha.append(str(numero % 2))
        numero //= 2

    return ''.join(reversed(pilha))

print(decimal_para_binario(10))   
print(decimal_para_binario(32))  



# 18. Implemente uma classe Fila com os métodos enqueue, dequeue, e is_Empty.
class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    def is_empty(self):
        return len(self.itens) == 0

f = Fila()
f.enqueue("A")
f.enqueue("B")
print("Saiu:", f.dequeue()) 
print("Está vazia?", f.is_empty())  



# 19. Use uma fila para simular um sistema de atendimento com prioridades 
# (fila normal e fila prioritária).
class Atendimento:
    def __init__(self):
        self.fila_normal = []
        self.fila_prioritaria = []

    def chegada(self, nome, prioridade=False):
        if prioridade:
            self.fila_prioritaria.append(nome)
        else:
            self.fila_normal.append(nome)

    def atender(self):
        if self.fila_prioritaria:
            return self.fila_prioritaria.pop(0)
        elif self.fila_normal:
            return self.fila_normal.pop(0)
        return None

sistema = Atendimento()
sistema.chegada("Cliente1")
sistema.chegada("Cliente2")
sistema.chegada("Cliente3", prioridade=True)
print("Atendido:", sistema.atender())  
print("Atendido:", sistema.atender()) 



# 20. Implemente uma fila circular com tamanho fixo 
# que sobrescreva elementos antigos quando cheia. 
class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.qtd = 0

    def enqueue(self, item):
        self.fila[self.fim] = item
        self.fim = (self.fim + 1) % self.tamanho
        if self.qtd < self.tamanho:
            self.qtd += 1
        else:
            self.inicio = (self.inicio + 1) % self.tamanho  # sobrescreve o mais antigo

    def dequeue(self):
        if self.qtd == 0:
            return None
        item = self.fila[self.inicio]
        self.inicio = (self.inicio + 1) % self.tamanho
        self.qtd -= 1
        return item

    def __str__(self):
        elementos = []
        i = self.inicio
        for _ in range(self.qtd):
            elementos.append(str(self.fila[i]))
            i = (i + 1) % self.tamanho
        return " <- ".join(elementos)

fc = FilaCircular(3)
fc.enqueue(1)
fc.enqueue(2)
fc.enqueue(3)
print(fc) 
fc.enqueue(4)  
print(fc)  
print("Saiu:", fc.dequeue()) 
print(fc)  