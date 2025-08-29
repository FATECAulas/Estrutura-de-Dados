# Crie 2 listas: 
# uma com 5 nomes(João, Maria, Kleber, Caio e Sarah) 
# e outra com 5 valores em reais(R$) correspondentes ao saldo da conta do usuário(2350.20; 540.50; 300.00; 830.15 e 150.00), 
# e usando laços de repetição imprima os dados da seguinte forma:

# Saída/Impressão:
#LISTA DE CLIENTES - BANCO XXXXXX
#NOME      SALDO
#nome0     saldo0
#nome1     saldo1

nome = ['João', 'Maria', 'Kleber', 'Caio', 'Sarah']
saldo = [2350.20, 540.50, 300.00, 830.15, 150.00]
print("Saída/Impressão:")
print("LISTA DE CLIENTES - BANCO XXXXXX")
print("NOME      SALDO")

for i in range(len(nome)):
    print(f"{nome[i]:<8} R$ {saldo[i]:.2f}")

# print(nome[0],"     R$",saldo[0])
# print(nome[1],"    R$",saldo[1])
# print(nome[2],"   R$",saldo[2])
# print(nome[3],"     R$",saldo[3])
# print(nome[4],"    R$",saldo[4]) 