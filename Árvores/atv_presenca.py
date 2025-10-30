# 1. Árvore AVL (inserção, remoção, rotações automáticas)
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def rebalance(node):
    update_height(node)
    bf = balance_factor(node)

    if bf > 1:
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    if bf < -1:
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node

def avl_insert(node, key):
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = avl_insert(node.left, key)
    elif key > node.key:
        node.right = avl_insert(node.right, key)
    else:
        return node  
    return rebalance(node)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def avl_remove(node, key):
    if not node:
        return None
    if key < node.key:
        node.left = avl_remove(node.left, key)
    elif key > node.key:
        node.right = avl_remove(node.right, key)
    else:
       
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
  
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = avl_remove(node.right, temp.key)
    if node:
        return rebalance(node)
    return None

def inorder(node):
    return inorder(node.left) + [node.key] + inorder(node.right) if node else []

# Exemplo:
root = None
for v in [20, 4, 15, 70, 50, 100, 90]:
    root = avl_insert(root, v)
print("AVL inorder:", inorder(root))
root = avl_remove(root, 70)
print("Depois de remover 70:", inorder(root))



# 2. N-Rainhas (recursivo + backtracking)
def solve_n_queens(n):
    solutions = []
    cols = set()
    diag1 = set()  
    diag2 = set()  
    board = ["."*n for _ in range(n)]
    board = [list(row) for row in board]

    def place(r):
        if r == n:
            solutions.append(["".join(line) for line in board])
            return
        for c in range(n):
            if c in cols or (r+c) in diag1 or (r-c) in diag2:
                continue
            cols.add(c); diag1.add(r+c); diag2.add(r-c)
            board[r][c] = 'Q'
            place(r+1)
            board[r][c] = '.'
            cols.remove(c); diag1.remove(r+c); diag2.remove(r-c)

    place(0)
    return solutions

# Exemplo:
sols = solve_n_queens(4)
print("Número de soluções para n=4:", len(sols))
for s in sols:
    print("\n".join(s))
    print()



# 3.Árvore de expressões — avaliar, derivar (simples) e simplificar
class Expr:
    def eval(self, env): raise NotImplementedError
    def diff(self, var): raise NotImplementedError
    def simplify(self): return self

class Const(Expr):
    def __init__(self, v): self.v = float(v)
    def eval(self, env): return self.v
    def diff(self, var): return Const(0)
    def __repr__(self): return str(int(self.v) if self.v.is_integer() else self.v)
    def simplify(self): return self

class Var(Expr):
    def __init__(self, name): self.name = name
    def eval(self, env): return env[self.name]
    def diff(self, var): return Const(1) if self.name == var else Const(0)
    def __repr__(self): return self.name

class Add(Expr):
    def __init__(self,a,b): self.a=a; self.b=b
    def eval(self,env): return self.a.eval(env)+self.b.eval(env)
    def diff(self,var): return Add(self.a.diff(var), self.b.diff(var)).simplify()
    def __repr__(self): return f"({self.a}+{self.b})"
    def simplify(self):
        a = self.a.simplify(); b = self.b.simplify()
        if isinstance(a, Const) and isinstance(b, Const): return Const(a.v+b.v)
        if isinstance(a, Const) and a.v==0: return b
        if isinstance(b, Const) and b.v==0: return a
        return Add(a,b)

class Sub(Expr):
    def __init__(self,a,b): self.a=a; self.b=b
    def eval(self,env): return self.a.eval(env)-self.b.eval(env)
    def diff(self,var): return Sub(self.a.diff(var), self.b.diff(var)).simplify()
    def __repr__(self): return f"({self.a}-{self.b})"
    def simplify(self):
        a=self.a.simplify(); b=self.b.simplify()
        if isinstance(a,Const) and isinstance(b,Const): return Const(a.v-b.v)
        if isinstance(b,Const) and b.v==0: return a
        return Sub(a,b)

class Mul(Expr):
    def __init__(self,a,b): self.a=a; self.b=b
    def eval(self,env): return self.a.eval(env)*self.b.eval(env)
    def diff(self,var):
        return Add(Mul(self.a.diff(var), self.b), Mul(self.a, self.b.diff(var))).simplify()
    def __repr__(self): return f"({self.a}*{self.b})"
    def simplify(self):
        a=self.a.simplify(); b=self.b.simplify()
        if isinstance(a,Const) and isinstance(b,Const): return Const(a.v*b.v)
        if (isinstance(a,Const) and a.v==0) or (isinstance(b,Const) and b.v==0): return Const(0)
        if isinstance(a,Const) and a.v==1: return b
        if isinstance(b,Const) and b.v==1: return a
        return Mul(a,b)

class Div(Expr):
    def __init__(self,a,b): self.a=a; self.b=b
    def eval(self,env): return self.a.eval(env)/self.b.eval(env)
    def diff(self,var):
        return Div(Sub(Mul(self.a.diff(var), self.b), Mul(self.a, self.b.diff(var))), Mul(self.b, self.b)).simplify()
    def __repr__(self): return f"({self.a}/{self.b})"
    def simplify(self):
        a=self.a.simplify(); b=self.b.simplify()
        if isinstance(a,Const) and isinstance(b,Const): return Const(a.v/b.v)
        if isinstance(a,Const) and a.v==0: return Const(0)
        if isinstance(b,Const) and b.v==1: return a
        return Div(a,b)

# Exemplo de uso:
x = Var('x')
f = Add(Add(Mul(x,x), Mul(Const(3), x)), Const(2))
print("f:", f)
print("f(2):", f.eval({'x':2}))
df = f.diff('x').simplify()
print("f':", df)
print("f'(2):", df.eval({'x':2}))



# 4. Mesclar duas BSTs ordenadas em uma única árvore balanceada
class Node:
    def __init__(self, key): self.key = key; self.left=None; self.right=None

def bst_inorder(root):
    return bst_inorder(root.left) + [root.key] + bst_inorder(root.right) if root else []

def merge_sorted(a,b):
    i=j=0; res=[]
    while i<len(a) and j<len(b):
        if a[i] < b[j]: res.append(a[i]); i+=1
        else: res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res

def sorted_list_to_bst(arr):
    if not arr: return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = sorted_list_to_bst(arr[:mid])
    root.right = sorted_list_to_bst(arr[mid+1:])
    return root

# Função principal
def merge_bsts(root1, root2):
    a = bst_inorder(root1)
    b = bst_inorder(root2)
    merged = merge_sorted(a,b)
    
    merged_nodups = []
    for x in merged:
        if not merged_nodups or merged_nodups[-1] != x:
            merged_nodups.append(x)
    return sorted_list_to_bst(merged_nodups)

def build_bst_from_list(vals):
    root = None
    for v in vals:
        if root is None:
            root = Node(v)
        else:
            cur = root
            while True:
                if v < cur.key:
                    if cur.left: cur = cur.left
                    else: cur.left = Node(v); break
                else:
                    if cur.right: cur = cur.right
                    else: cur.right = Node(v); break
    return root

r1 = build_bst_from_list([1,3,5])
r2 = build_bst_from_list([2,4,6,7])
merged_root = merge_bsts(r1, r2)
print("Merged inorder:", bst_inorder(merged_root))



# 5. Trie (Prefix Tree) com insert, search, remove, autocomplete
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch, TrieNode())
        cur.end = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children: return False
            cur = cur.children[ch]
        return cur.end

    def starts_with(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children: return None
            cur = cur.children[ch]
        return cur

    def remove(self, word):
        def _remove(node, w, i):
            if i == len(w):
                if not node.end: return False
                node.end = False
                return len(node.children) == 0
            ch = w[i]
            if ch not in node.children: return False
            can_delete = _remove(node.children[ch], w, i+1)
            if can_delete:
                del node.children[ch]
                return not node.end and len(node.children) == 0
            return False
        _remove(self.root, word, 0)

    def autocomplete(self, prefix):
        start = self.starts_with(prefix)
        if not start: return []
        results = []
        def dfs(node, path):
            if node.end:
                results.append(prefix + path)
            for ch, child in node.children.items():
                dfs(child, path+ch)
        dfs(start, "")
        return results

# Exemplo:
t = Trie()
for w in ["car", "card", "care", "dog", "doom"]:
    t.insert(w)
print("search 'card':", t.search("card"))
print("autocomplete 'ca':", t.autocomplete("ca"))
t.remove("card")
print("search 'card' após remoção:", t.search("card"))



# 6. Dijkstra usando heap binário (heapq) — caminho mais curto em grafo
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d,u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v,w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, prev

def shortest_path(prev, start, target):
    if prev[target] is None and start != target and target not in prev:
        return None
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

# Exemplo:
g = {
    'A': [('B',1),('C',4)],
    'B': [('C',2),('D',5)],
    'C': [('D',1)],
    'D': []
}
dist, prev = dijkstra(g, 'A')
print("Distâncias:", dist)
print("Caminho A->D:", shortest_path(prev, 'A', 'D'))