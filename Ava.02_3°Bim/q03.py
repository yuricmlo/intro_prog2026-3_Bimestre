# Estrutura: Tupla (não pode ser modificada depois de feita)
# Solução: vou fazer uma lista que guarda tuplas

pontos = []

for i in range(1, 4):
    x = float(input(f"X {i}:"))
    y = float(input(f"Y {i}:"))
    pontos.append((x, y)) # adiciono as duas variáveis

print("Pontos Cadastrados:")
for p in pontos:
    print(f"- {p}")

for i in range(3): # são 3 pontos
    x, y = pontos[i] # descompactar 
    if x > 0 and y > 0:
        quadrante = 1
    elif x < 0 and y > 0:
        quadrante = 2
    elif x < 0 and y < 0:
        quadrante = 3
    elif x > 0 and y < 0:
        quadrante = 4
    else:
        quadrante = 0 # sobre um dos eixos

    print(f"Pontos {pontos[i]}", end= " ")

    if quadrante == 0:
        print("Está sobre um dos eixos.")
    else:
        print(f"está no {quadrante}º quadrante.")
    
    