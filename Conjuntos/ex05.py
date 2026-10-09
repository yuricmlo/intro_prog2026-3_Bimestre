import random

numeros = []
for i in range(101):
    numeros.append(random.randint(0,100)) 
print(numeros)
print(f"Números diferentes: {len(set(numeros))}")

# O randint inclui o 100 ao ivés de ir só até 99.