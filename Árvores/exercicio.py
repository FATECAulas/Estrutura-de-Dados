# Os 3 algoritmos de percurso em árvores binárias são definidos e implementados
# recursivamente, pois esta é a forma mais natural de se realizá-los, já que a
# árvore está próxima à definição destes.
# Redefina os algoritmos de percurso de forma iterativa, usando um algoritmo
# com um laço e uma pilha para simular a recursividade.
def construir_arvore(n):
    if n == 0:
        return None

    valor = int(input("Valor do nó: "))
    nodo = {"valor": valor}

    nodo["esq"] = construir_arvore(n // 2)
    nodo["dir"] = construir_arvore(n - n // 2 - 1)

    return nodo

# Exemplo de uso
n = int(input("Quantos nós terá a árvore? "))
raiz = construir_arvore(n)


def preordem_iterativo(raiz):
    if raiz is None:
        return
    
    pilha = [raiz]
    
    while pilha:
        nodo = pilha.pop()
        print(nodo["valor"], end=" ")  # Processa o nó
        
        if nodo["dir"]:
            pilha.append(nodo["dir"])
        if nodo["esq"]:
            pilha.append(nodo["esq"])


def emordem_iterativo(raiz):
    pilha = []
    nodo = raiz
    
    while pilha or nodo:
        while nodo:
            pilha.append(nodo)
            nodo = nodo["esq"]
        
        nodo = pilha.pop()
        print(nodo["valor"], end=" ")  # Processa o nó
        
        nodo = nodo["dir"]


def posordem_iterativo(raiz):
    if raiz is None:
        return
    
    pilha1 = [raiz]
    pilha2 = []
    
    while pilha1:
        nodo = pilha1.pop()
        pilha2.append(nodo)
        
        if nodo["esq"]:
            pilha1.append(nodo["esq"])
        if nodo["dir"]:
            pilha1.append(nodo["dir"])
    
    while pilha2:
        nodo = pilha2.pop()
        print(nodo["valor"], end=" ")  # Processa o nó