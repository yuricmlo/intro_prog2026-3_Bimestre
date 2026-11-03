# Estrutura : Tupla / Lista
# A ordem importa e podem ter valores repetidos

tempos = [] 
for i in range(1, 6):
    tempo = float(input(f"Tempo {i}:"))
    tempos.append(tempo)

for t in tempos:
    print(f"- {t} segundos.")
print(f"Menor tempo: {min(tempos)} segundos.")
print(f"Maior tempo: {max(tempos)} segundos.")
print(f"Média dos tempos: {sum(tempos) / len(tempos)} segundos.")
print(f"Posição do primeiro tempo mais rápido: {tempos.index(min(tempos))+1} segundos.")

# +1 serve para ele exibir as posições na visão do ser humano (ex: posição 1, posição 2; ao invés de posição 0, posição 1, posição 2...)