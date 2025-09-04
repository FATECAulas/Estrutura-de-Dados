#Exercício: 
# – Crie um programa que gerencie uma PILHAde TAREFAS a serem cumpridas. 
# As tarefas são Strings que descrevem uma ação a ser executada. 
# – O usuário deverá ter duas opções: 
# • Inserir tarefa na pilha;
# • Obter a próxima tarefa da pilha.

class Stack: # construir
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]

pilha = Stack()

while True:
    print("\nGERENCIADOR DE TAREFAS")
    print("1 - Inserir Tarefa")
    print("2 - Próximo Tarefa")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
            tarefa = input("Tarefa: ")
            pilha.push(tarefa)
            print("Tarefa Adicionado")

    elif opcao == "2":
        if not pilha.isEmpty():
            tarefa = pilha.peek()
            print(f"Tarefa: {tarefa}")
        else:
            print("Nenhuma Tarefa")
    
    elif opcao == "3":
        break

    else:
        print("Opção inválida")