# 1: Crie uma classe Grafo em Python que possa representar grafos usando a lista de
# adjacências. A classe deve ser capaz de ser inicializada como um grafo direcionado ou
# não direcionado e permitir a adição de vértices.



# 2: Implemente o método adicionar_aresta(u, v, peso=1) na classe Grafo que adiciona
# uma aresta entre os vértices u e v. A aresta deve suportar pesos.



# 3: Adicione um método existe_aresta(u, v) à classe Grafo que retorna True se houver
# uma aresta entre u e v, e False caso contrário.



# 4: Implemente o método remover_aresta(u, v) que remove uma aresta entre os
# vértices u e v da classe Grafo.



# 5: Para grafos não direcionados, implemente um método grau_vertice(vertice) que
# retorna o grau de um vértice.



# 6: Para grafos direcionados, implemente métodos grau_entrada(vertice) e
# grau_saida(vertice) que retornam o grau de entrada e saída, respectivamente.



# 7: Crie um método listar_vizinhos(vertice) que retorna uma lista de todos os vértices
# adjacentes a um dado vértice.



# 8: Adicione métodos numero_vertices() e numero_arestas() para retornar a
# quantidade total de vértices e arestas no grafo.



# 9: Implemente um método imprimir_grafo() que exiba a representação atual do grafo
# (usando listas de adjacência) de forma legível.



# 10: Para um grafo não direcionado, implemente um método eh_conexo() que verifica
# se o grafo é conexo.



# 11 Problema: Crie uma classe Grafo em Python que represente um grafo não
# direcionado usando uma lista de adjacência. A classe deve ser capaz de:
# 1. Inicializar um grafo vazio.
# 2. Adicionar vértices ao grafo.
# 3. Adicionar arestas entre dois vértices, considerando que a relação é simétrica
# (não direcionada).



# 12: Problema: Crie uma classe GrafoDirecionado em Python que represente um grafo
# direcionado usando uma matriz de adjacência. A classe deve ser capaz de:
# 1. Inicializar o grafo com um número pré-definido de vértices (assuma que os
# vértices são inteiros de 0 a num_vertices - 1).
# 2. Adicionar arestas direcionadas de um vértice de origem u para um vértice de
# destino v.



# 13: Problema: Aprimore as classes Grafo (não direcionado, Questão 11) e
# GrafoDirecionado (direcionado, Questão 12) para incluir métodos de cálculo de grau:
# 1. Para Grafo (não direcionado): grau(vertice) que retorna o número de arestas
# incidentes no vértice.
# 2. Para GrafoDirecionado (direcionado): grau_entrada(vertice) e
# grau_saida(vertice) que retornam o número de arestas que chegam e saem do
# vértice, respectivamente.



# 14: Problema: Modifique a classe GrafoDirecionado (da Questão 12/13) para suportar
# arestas ponderadas. A matriz de adjacência deve armazenar os pesos das arestas.
# 1. O método adicionar_aresta(u, v, peso) agora deve aceitar um peso e armazenálo na matriz.
# 2. Adicione um método obter_peso_aresta(u, v) que retorna o peso da aresta de
# u para v. Se a aresta não existir ou os vértices forem inválidos, deve retornar
# None.
# 3. Adicione um método e_adjacente(u, v) que retorna True se houver uma aresta
# (com qualquer peso) de u para v, e False caso contrário.



# 15: Problema: Na classe Grafo (não direcionado, da Questão 11/13), implemente um
# método caminho_mais_curto_bfs(inicio, fim) que utilize a Busca em Largura (BFS) para
# encontrar e retornar a lista de vértices que formam o caminho mais curto (em termos
# do número de arestas) entre inicio e fim. Se não houver caminho, retorne uma lista
# vazia.



# 16: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15), implemente
# um método contem_ciclo() que retorne True se o grafo contiver pelo menos um ciclo,
# e False caso contrário.



# 17: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16),
# implemente um método e_conexo() que retorne True se o grafo for conexo (ou seja, se
# houver um caminho entre cada par de vértices), e False caso contrário.



# 18: Problema: Na classe GrafoDirecionadoPonderado (da Questão 14), implemente um
# método e_fortemente_conexo() que retorne True se o grafo direcionado for
# fortemente conexo, e False caso contrário. Um grafo direcionado é fortemente conexo
# se existir um caminho de u para v e de v para u para qualquer par de vértices u, v.



# 19: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16/17),
# implemente um método e_clique(subconjunto_vertices) que receba uma lista de
# vértices e retorne True se esse subconjunto formar um clique (ou seja, cada par de
# vértices no subconjunto está conectado por uma aresta), e False caso contrário.



# 20: Problema: Na classe Grafo (não direcionado, da Questão 11/13/15/16/17/19),
# implemente um método componentes_conexos() que retorne uma lista de listas, onde
# cada sub-lista representa um componente conexo do grafo.