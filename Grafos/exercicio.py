# 1: Crie uma classe Grafo em Python que possa representar grafos usando a lista de
# adjacências. A classe deve ser capaz de ser inicializada como um grafo direcionado ou
# não direcionado e permitir a adição de vértices.
def adicionar_vertice(grafo, v):
    if v not in grafo:
        grafo[v] = {}
    return grafo

if __name__ == "__main__":
    g = {}
    adicionar_vertice(g, "A")
    adicionar_vertice(g, "B")
    print("Vertices:", list(g.keys()))  # -> ['A','B']


# 2: Implemente o método adicionar_aresta(u, v, peso=1) na classe Grafo que adiciona
# uma aresta entre os vértices u e v. A aresta deve suportar pesos.
def adicionar_aresta(grafo, u, v, peso=1):
    if u not in grafo: grafo[u] = {}
    if v not in grafo: grafo[v] = {}
    grafo[u][v] = peso
    grafo[v][u] = peso

if __name__ == "__main__":
    g = {}
    adicionar_aresta(g, "A", "B")
    adicionar_aresta(g, "B", "C", peso=5)
    print(g)  # {'A': {'B':1}, 'B': {'A':1,'C':5}, 'C': {'B':5}}


# 3: Adicione um método existe_aresta(u, v) à classe Grafo que retorna True se houver
# uma aresta entre u e v, e False caso contrário.
def existe_aresta(grafo, u, v):
    return u in grafo and v in grafo[u]

if __name__ == "__main__":
    g = {"A":{"B":1}, "B":{"A":1}}
    print(existe_aresta(g, "A", "B"))  # True
    print(existe_aresta(g, "A", "C"))  # False


# 4: Implemente o método remover_aresta(u, v) que remove uma aresta entre os
# vértices u e v da classe Grafo.
def remover_aresta(grafo, u, v):
    if u in grafo and v in grafo[u]:
        del grafo[u][v]
    if v in grafo and u in grafo[v]:
        del grafo[v][u]

if __name__ == "__main__":
    g = {"A":{"B":1}, "B":{"A":1,"C":2}, "C":{"B":2}}
    remover_aresta(g, "B", "C")
    print(g)  # C não conectado a B


# 5: Para grafos não direcionados, implemente um método grau_vertice(vertice) que
# retorna o grau de um vértice.
def grau_vertice(grafo, v):
    if v not in grafo: return 0
    return len(grafo[v])

if __name__ == "__main__":
    g = {"A":{"B":1,"C":1}, "B":{"A":1}}
    print(grau_vertice(g, "A"))  # 2


# 6: Para grafos direcionados, implemente métodos grau_entrada(vertice) e
# grau_saida(vertice) que retornam o grau de entrada e saída, respectivamente.
def grau_saida(grafo, v):
    return len(grafo.get(v, {}))

def grau_entrada(grafo, v):
    cnt = 0
    for u in grafo:
        if v in grafo[u]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"C":1},"C":{}}
    print("saida A:", grau_saida(g, "A"), "entrada B:", grau_entrada(g, "B"))


# 7: Crie um método listar_vizinhos(vertice) que retorna uma lista de todos os vértices
# adjacentes a um dado vértice.
def listar_vizinhos(grafo, v):
    return list(grafo.get(v, {}).keys())

if __name__ == "__main__":
    g = {"A":{"B":1,"C":1}}
    print(listar_vizinhos(g, "A"))  # ['B','C']


# 8: Adicione métodos numero_vertices() e numero_arestas() para retornar a
# quantidade total de vértices e arestas no grafo.
def numero_vertices(grafo):
    return len(grafo)

def numero_arestas(grafo):
    total = sum(len(vs) for vs in grafo.values())
    return total // 2  # porque contado duas vezes

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"A":1,"C":1},"C":{"B":1}}
    print("V:", numero_vertices(g), "E:", numero_arestas(g))


# 9: Implemente um método imprimir_grafo() que exiba a representação atual do grafo
# (usando listas de adjacência) de forma legível.
def imprimir_grafo(grafo):
    for v in grafo:
        viz = ", ".join(f"{u}(p={grafo[v][u]})" for u in grafo[v])
        print(f"{v} -> {viz}")

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"A":1,"C":2},"C":{"B":2}}
    imprimir_grafo(g)


# 10: Para um grafo não direcionado, implemente um método eh_conexo() que verifica
# se o grafo é conexo.
from collections import deque

def eh_conexo(grafo):
    if not grafo: return True
    inicio = next(iter(grafo))
    visit = set()
    q = deque([inicio])
    while q:
        u = q.popleft()
        if u in visit: continue
        visit.add(u)
        for w in grafo[u]:
            if w not in visit:
                q.append(w)
    return len(visit) == len(grafo)

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"A":1},"C":{}}  # desconexo
    print(eh_conexo(g))  # False


# 11 Problema: Crie uma classe Grafo em Python que represente um grafo não
# direcionado usando uma lista de adjacência. A classe deve ser capaz de:
# 1. Inicializar um grafo vazio.
# 2. Adicionar vértices ao grafo.
# 3. Adicionar arestas entre dois vértices, considerando que a relação é simétrica
# (não direcionada).
def adicionar_aresta(grafo, u, v, peso):
    if u not in grafo: grafo[u] = {}
    if v not in grafo: grafo[v] = {}
    grafo[u][v] = peso
    grafo[v][u] = peso

def obter_peso(grafo, u, v):
    return grafo.get(u, {}).get(v)

if __name__ == "__main__":
    g = {}
    adicionar_aresta(g, "X", "Y", 3.14)
    print("peso X-Y:", obter_peso(g, "X", "Y"))


# 12: Problema: Crie uma classe GrafoDirecionado em Python que represente um grafo
# direcionado usando uma matriz de adjacência. A classe deve ser capaz de:
# 1. Inicializar o grafo com um número pré-definido de vértices (assuma que os
# vértices são inteiros de 0 a num_vertices - 1).
# 2. Adicionar arestas direcionadas de um vértice de origem u para um vértice de
# destino v.
class MatrizDirecionada:
    def __init__(self, n):
        self.n = n
        self.mat = [[0]*n for _ in range(n)]
    def adicionar_aresta(self, u, v):
        self.mat[u][v] = 1
    def e_adjacente(self, u, v):
        return self.mat[u][v] == 1

if __name__ == "__main__":
    m = MatrizDirecionada(3)
    m.adicionar_aresta(0,1)
    print(m.e_adjacente(0,1), m.e_adjacente(1,0))  # True False


# 13: Problema: Aprimore as classes Grafo (não direcionado, Questão 11) e
# GrafoDirecionado (direcionado, Questão 12) para incluir métodos de cálculo de grau:
# 1. Para Grafo (não direcionado): grau(vertice) que retorna o número de arestas
# incidentes no vértice.
# 2. Para GrafoDirecionado (direcionado): grau_entrada(vertice) e
# grau_saida(vertice) que retornam o número de arestas que chegam e saem do
# vértice, respectivamente.
def grau_saida(mat, v):
    return sum(mat[v])

def grau_entrada(mat, v):
    return sum(row[v] for row in mat)

if __name__ == "__main__":
    mat = [
        [0,1,0],
        [0,0,1],
        [0,0,0]
    ]
    print("saida 0:", grau_saida(mat,0), "entrada 2:", grau_entrada(mat,2))


# 14: Problema: Modifique a classe GrafoDirecionado (da Questão 12/13) para suportar
# arestas ponderadas. A matriz de adjacência deve armazenar os pesos das arestas.
# 1. O método adicionar_aresta(u, v, peso) agora deve aceitar um peso e armazenálo na matriz.
# 2. Adicione um método obter_peso_aresta(u, v) que retorna o peso da aresta de
# u para v. Se a aresta não existir ou os vértices forem inválidos, deve retornar
# None.
# 3. Adicione um método e_adjacente(u, v) que retorna True se houver uma aresta
# (com qualquer peso) de u para v, e False caso contrário.
class MatrizPonderada:
    def __init__(self,n):
        self.n = n
        self.mat = [[None]*n for _ in range(n)]
    def adicionar(self,u,v,p):
        self.mat[u][v] = p
    def peso(self,u,v):
        return self.mat[u][v]

if __name__ == "__main__":
    mp = MatrizPonderada(3)
    mp.adicionar(0,1,2.5)
    print("peso 0->1:", mp.peso(0,1))


# 15: Problema: Na classe Grafo (não direcionado, da Questão 11/13), implemente um
# método caminho_mais_curto_bfs(inicio, fim) que utilize a Busca em Largura (BFS) para
# encontrar e retornar a lista de vértices que formam o caminho mais curto (em termos
# do número de arestas) entre inicio e fim. Se não houver caminho, retorne uma lista
# vazia.
from collections import deque
def caminho_bfs(grafo, inicio, fim):
    if inicio not in grafo or fim not in grafo: return []
    pai = {inicio: None}
    q = deque([inicio])
    while q:
        u = q.popleft()
        if u == fim: break
        for v in grafo[u]:
            if v not in pai:
                pai[v] = u
                q.append(v)
    if fim not in pai: return []
    path = []
    cur = fim
    while cur is not None:
        path.append(cur); cur = pai[cur]
    path.reverse()
    return path

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"A":1,"C":1},"C":{"B":1}}
    print(caminho_bfs(g,"A","C"))  # ['A','B','C']


# 16: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15), implemente
# um método contem_ciclo() que retorne True se o grafo contiver pelo menos um ciclo,
# e False caso contrário.
def contem_ciclo(grafo):
    visit = set()
    def dfs(u, p):
        visit.add(u)
        for v in grafo[u]:
            if v == p: continue
            if v in visit: return True
            if dfs(v, u): return True
        return False
    for v in grafo:
        if v not in visit:
            if dfs(v, None): return True
    return False

if __name__ == "__main__":
    g1 = {"A":{"B":1},"B":{"A":1,"C":1},"C":{"B":1}}  # sem ciclo
    g2 = {"A":{"B":1,"C":1},"B":{"A":1,"C":1},"C":{"A":1,"B":1}}  # ciclo
    print(contem_ciclo(g1), contem_ciclo(g2))  # False True


# 17: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16),
# implemente um método e_conexo() que retorne True se o grafo for conexo (ou seja, se
# houver um caminho entre cada par de vértices), e False caso contrário.
def eh_arvore(grafo):
    # conectado?
    if not grafo: return True
    # checar conexidade
    visited = set()
    stack = [next(iter(grafo))]
    while stack:
        u = stack.pop()
        if u in visited: continue
        visited.add(u)
        for v in grafo[u]:
            if v not in visited:
                stack.append(v)
    if len(visited) != len(grafo): 
        return False
    # checar ciclo (usa função do exer16)
    def contem_ciclo(g):
        vis = set()
        def dfs(u,p):
            vis.add(u)
            for w in g[u]:
                if w==p: continue
                if w in vis: return True
                if dfs(w,u): return True
            return False
        for x in g:
            if x not in vis:
                if dfs(x,None): return True
        return False
    return not contem_ciclo(grafo)

if __name__ == "__main__":
    tree = {"A":{"B":1},"B":{"A":1,"C":1},"C":{"B":1}}
    print(eh_arvore(tree))  # True


# 18: Problema: Na classe GrafoDirecionadoPonderado (da Questão 14), implemente um
# método e_fortemente_conexo() que retorne True se o grafo direcionado for
# fortemente conexo, e False caso contrário. Um grafo direcionado é fortemente conexo
# se existir um caminho de u para v e de v para u para qualquer par de vértices u, v.
def kosaraju_fortemente_conexo(adj):
    n = len(adj)
    visited = [False]*n
    order = []
    def dfs1(u):
        visited[u]=True
        for v in adj[u]:
            if not visited[v]: dfs1(v)
        order.append(u)
    for i in range(n):
        if not visited[i]: dfs1(i)
    # transposto
    tadj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            tadj[v].append(u)
    comp = [False]*n
    def dfs2(u):
        comp[u]=True
        for v in tadj[u]:
            if not comp[v]: dfs2(v)
    dfs2(order[-1])
    return all(comp)

if __name__ == "__main__":
    adj1 = [[1],[2],[0]]  # 0->1->2->0, fortemente conexo
    adj2 = [[1],[2],[]]   # não fortemente conexo
    print(kosaraju_fortemente_conexo(adj1), kosaraju_fortemente_conexo(adj2))


# 19: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16/17),
# implemente um método e_clique(subconjunto_vertices) que receba uma lista de
# vértices e retorne True se esse subconjunto formar um clique (ou seja, cada par de
# vértices no subconjunto está conectado por uma aresta), e False caso contrário.
def e_clique(grafo, vertices):
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            u = vertices[i]; v = vertices[j]
            if v not in grafo.get(u, {}):
                return False
    return True

if __name__ == "__main__":
    g = {"A":{"B":1,"C":1},"B":{"A":1,"C":1},"C":{"A":1,"B":1}}
    print(e_clique(g, ["A","B","C"]))  # True
    print(e_clique(g, ["A","B"]))  # True


# 20: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16/17/19),
# implemente um método componentes_conexos() que retorne uma lista de listas, onde
# cada sub-lista representa um componente conexo do grafo.
from collections import deque
def componentes_conexos(grafo):
    visit = set()
    comps = []
    for v in grafo:
        if v in visit: continue
        comp = []
        q = deque([v])
        while q:
            u = q.popleft()
            if u in visit: continue
            visit.add(u)
            comp.append(u)
            for w in grafo[u]:
                if w not in visit:
                    q.append(w)
        comps.append(comp)
    return comps

if __name__ == "__main__":
    g = {"A":{"B":1},"B":{"A":1},"C":{"D":1},"D":{"C":1},"E":{}}
    print(componentes_conexos(g))  # [['A','B'], ['C','D'], ['E']]