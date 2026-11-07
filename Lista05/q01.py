estoque = [100]

n = int(input("Quantidade de operações:"))

for i in range(1, n+1):
    operacao = int(input())
    valor = estoque + operacao
    estoque.append(operacao)
    

print(estoque)
