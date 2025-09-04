class Queue: #construir
    def __init__(self):
        self.items = []
    def isEmpty(self): #testar
        return self.items == []
    def enqueue(self, item): #adicionar
        self.items.insert(0,item)
    def dequeue(self): #remover
        return self.items.pop()
    def size(self): #tamanho
        return len(self.items)

q=Queue()

q.enqueue(4) 
q.enqueue('dog')
q.enqueue(True)
print(q.size()) #(3)