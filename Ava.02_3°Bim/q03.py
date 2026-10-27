# Estrutura: Tupla (não pode ser modificada depois de alterada)
# Solução: vou fazer uma lista que guarda tuplas

pontos = []

for i in range(1, 4):
    x = float(input(f"X {i}:"))
    y = float(input(f"Y {i}:"))
    pontos.append((x, y)) # adiciono as duas variáveis

print("Pontos Cadastrados:")
for p in pontos:
    print(f"- {p}")

for i in range(len(3)): # são 3 pontos
    x, y = pontos[i]
    if x > 0 and y > 0:
        quadrante = 1
    elif x < 0 and y > 0:
        quadrante = 2
    elif x < 0 and y < 0:
        quadrante = 3
    elif x > 0 and y < 0:
        quadrante = 0

    print(f"Pontos {pontos[i]}", end= " ")

    if quadrante == 0:
        print("Está sobre um dos eixos.")
    # tem mais código que tenho que adicionar (está no repositório do professor)
    