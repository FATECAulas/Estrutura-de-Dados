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

# 5. Crie uma função Quick Sort que ordene uma lista de números 
# e retorne o número de comparações realizadas.

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

# 8. Crie uma versão do Insertion Sort que ordene três listas 
# pelo segundo elemento de cada lista.

# 9. Desenvolva uma comparação de tempo de execução entre 
# Bubble Sort e Quick Sort para uma lista de 1000 elementos.

# 10. Implemente o Merge Sort iterativo para ordenar uma lista de números.

# 11. Crie uma função que remova todos os elementos duplicados de uma lista 
# mantendo a ordem original dos elementos.

# 12. Desenvolva uma função que encontre o segundo maior elemento em uma lista 
# sem usar funções de ordenação.

# 13. Implemente uma função que inverta uma lista.

# 14. Crie uma função que mescle duas listas ordenadas em uma única lista ordenada.

# 15. Implemente uma classe Pilha com os métodos push, pop, e is_Empty.

# 16. Use uma pilha para verificar se uma expressão com parênteses está balanceada.

# 17. Crie uma função que converta um número decimal para binário usando uma pilha.

# 18. Implemente uma classe Fila com os métodos enqueue, dequeue, e is_Empty.

# 19. Use uma fila para simular um sistema de atendimento com prioridades 
# (fila normal e fila prioritária).

# 20. Implemente uma fila circular com tamanho fixo 
# que sobrescreva elementos antigos quando cheia. 