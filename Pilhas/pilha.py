class Stack: # construir
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s=Stack()

print(s.isEmpty()) #testar | (True)
s.push(4) #adicionar
s.push('dog')
print(s.peek()) #retorna o item no topo | (dog)
s.push(True)
print(s.size()) #tamanho | (3)
print(s.isEmpty()) #(False)
s.push(8.4)
print(s.pop()) #remover | (8.4)
print(s.pop()) #(True)
print(s.size()) #(2)