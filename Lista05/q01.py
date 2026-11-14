estoque = [100]

n = int(input("Quantidade de operações:"))

for i in range(1, n+1):
    operacao = int(input(f"Operação: {i}"))  
    valor = estoque[-1] + operacao # calcula o valor do estoque atual
    estoque.append(valor)

    if valor < 0:
        print(f"Estoque negativo pela 1ª vez na operação {i}")
        print(f"Estoque no momento do erro {estoque[-1]}")
    
        break

print(f"Estoque final: {estoque[-1]}")
print(f"Maior estoque registrado: {max(estoque)}")
print(f"Menor estoque registrado: {min(estoque)}")


