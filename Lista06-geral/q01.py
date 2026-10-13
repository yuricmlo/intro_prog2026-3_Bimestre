# Estrutura: Lista, pois mantém a ordem dos elementos, aceita repetições e é mutável.

notas = []

for i in range(1, 9):
    nota = int(input(f"Digite a nota {i}:"))
    notas.append(nota)

print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}.")
print(f"Médias das notas: {sum(notas) / len(notas):.0f}.")

posicao = int(input("Digite qual nota deseja alterar (1-8):"))

if 1 <= posicao <= 8:
    nova_nota = int(input("Digite a nova nota:"))
    notas[posicao-1] = nova_nota
    print(notas)
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}.")
    print(f"Médias das notas: {sum(notas) / len(notas):.0f}.")

else:
    print("Opção inválida!")
