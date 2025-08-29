lista = []
print(lista)

lista = [10, 15, 20, 25, 30]
print(lista)
print(lista[0]) #retornara o valor 10
print(len(lista)) #retorna 5 (o tamanho da lista)
lista[0] = 8 #troca o 10 pelo 8
print(lista)

# ---------------------------------------------------------
A = [3, 7.5, 'txt']
print(A)
print(A[0])
print(A[1])
print(A[2])
del (A[1]) #del = deleta
print(A) #retorna [3, 'txt']

# ---------------------------------------------------------
L = [10, 15, 20, 25,30]
A = [3, 7.5, 'txt']
X = L[0] + A[1] #soma os valores
print(X) #retorna 17.5

X = L + A #junta as listas
print(X) #retorna [10, 15, 20, 25, 30, 3, 7.5, 'txt']

# ---------------------------------------------------------
L = [1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23]
print(L[0:3]) # retorna [1, 3, 5]
print(L[4:10]) #retorna [11, 13, 15, 17, 19, 21]
print(L[:5]) #retorna [1, 3, 5, 9, 11]
print(L[5:]) #retorna [13, 15, 17, 19, 21, 23]
print (L[0:8:3]) #retorna [1, 9, 15]
print(L[::4]) #retorna [1, 11, 19]

# ------------------MULTIPLICADOR---------------------------
A = [3, 7] * 3
print(A) #retorna [3, 7, 3, 7, 3, 7]

L = [5] * 10
print(L) #retorna [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

# ---------------------------------------------------------
S = "Um texto"
L = list(S)
print(L) #retorna ['U', 'm', ' ', 't', 'e', 'x', 't', 'o']
L = S.split()
print(L) #retorna ['Um', 'texto']

S = "5;7;8;8.8;12"
L = S.split(";")
print(L) #retorna ['5', '7', '8', '8.8', '12']

# ----------------------OPERADOR IN-------------------------
L = [3, 6, 9]
print(9 in L) #retorna True
print(5 in L) #False
print(5 not in L) #True

Caes = ["Labrador", "Poodle", "Terrier"]
a = "Lassie"
if a in Caes:
    print("Boa escolha")
else:
    print("Não temos essa raça") #retorna o else
    
# ---------------------------------------------------------
L = [3, 6, 9]
L.append(2) #adiciona ao final da lista
print(L) #[3, 6, 9, 2]
L.insert(2, 15) #adiciona o 15 na posição 2
print(L) #[3, 6, 15, 9, 2]
L.append(6)
print(L) #[3, 6, 15, 9, 2, 6]
print(L.count(6)) #quantidade de vezes que o número aparace | 2
print(L.index(9)) #mostra a posição do número | 3
print(L.pop(3)) #remove o indice que ele esta se referindo | 9
print(L) #[3, 6, 15, 2, 6]
L.remove(6) 
print(L) #[3, 15, 2, 6]

A = [22, 32, 42]
L.extend(A)
print(L) #[3, 15, 2, 6, 22, 32, 42]
L.reverse() #inverte a lista
print(L) #[42, 32, 22, 6, 2, 15, 3]
L.sort() #ordem crescente
print(L) #[2, 3, 6, 15, 22, 32, 42]
L.sort(reverse=True) #ordem decrecente
print(L) #[42, 32, 22, 15, 6, 3, 2]
L.clear()
L = ["dado", "uva", "caixa", "lata", "casa"]
L.sort()
print(L) #['caixa', 'casa', 'dado', 'lata', 'uva']

# ---------------------------------------------------------
L = [2, 4, 6, 8, 10]
V = L
V[0] = 15 #troca o 2 por 15
print(V)
print(L) 
print(id(L)) #2636044337920
print(id(V)) #2636044337920 | id L e V iguais
C = L.copy()
print(id(C)) #2636045935552 | id C diferente
C[0] = 2
print(C) #[2, 4, 6, 8, 10]
print(L) #[15, 4, 6, 8, 10]

# ---------------------------------------------------------
L = [[2, 4, 6], [1, 2, 3]]
L[0]
print(L[1]) #[1, 2, 3]
print(L[1] [0]) #1
print(L[1] [2]) #3
A = [7, 8, 9, 10]
L.append(A)
print(L) #[[2, 4, 6], [1, 2, 3], [7, 8, 9, 10]]

# ---------------------------------------------------------
L = [[1,2,['3,1', '3,2',['3.3.1',['3.3.2.1', '3.3.2.2'], '3.3.3']]], [4,5,6]]
print(L[0]) #[[1,2,['3,1', '3,2',['3.3.1',['3.3.2.1', '3.3.2.2'], '3.3.3']]]
print(L[0] [2]) #['3,1', '3,2', ['3.3.1', ['3.3.2.1', '3.3.2.2'], '3.3.3']]
print(L[0] [2] [2]) #['3.3.1', ['3.3.2.1', '3.3.2.2'], '3.3.3']
print(L[0] [2] [2] [1]) #['3.3.2.1', '3.3.2.2']