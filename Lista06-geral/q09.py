# Estrutura: Listas para poder adicionar novos pontos, Tuplas para evitar a modificação e Conjuntos
# para poder filtrar os elementos repetidos

num_pontos = []

p = int(input("Digite quantos pontos vão ser registrados:"))

for ponto in range(p):
    valor_x = int(input("Digite o valor de x deste ponto:"))
    valor_y = int(input("Digite o valor de y deste ponto:"))
    ponto_atual = (valor_x, valor_y)
    num_pontos.append(ponto_atual)

print(f"1º Ponto: {num_pontos[0]}")
print(f"Último ponto: {num_pontos[-1]}")
print(f"Quantidade total de posições registradas: {len(num_pontos)}")
print(f"Posições diferentes que o robô visitou: {len(set(num_pontos))}")