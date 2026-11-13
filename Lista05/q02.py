n = int(input("Quantidade de alunos:"))
medias = []
situacoes = [0, 0, 0] # 0 -> aprovados, 1 -> provas finais, 2 - > reprovados

for aluno in range(1, n+1): # 1...n sem excluir
    print(f"== Aluno {aluno} ==") # +1 serve para começar a contagem em 1
    nota1 = int(input("\tNota 1:")) # \t serve para organização
    nota2 = int(input("\tNota 2:"))
    media = (nota1 + nota2) / 2 
    medias.append(media)
    print(f"Média = {media:.0f} ", end="") # imprime nessa mesma linha e média e a situação

    if media >= 60:
        print("Aprovado")
        situacoes[0] += 1 # i = i + 1 ==>  += 1

    elif media >= 20:
        print("Prova Final")
        situacoes[1] += 1

    else:
        print("Reprovado")
        situacoes[2] += 1


media_geral = sum(medias) / len(medias)

percentual_aprovados = (situacoes[0] / n) * 100 

print(f"Maior média = {max(medias):.0f}")
print(f"Menor média = {min(medias):.0f}")
print(f"Média geral = {media_geral:.0f}")
print(f"Aprovados: {situacoes[0]}")
print(f"Prova Final: {situacoes[1]}")
print(f"Rerovados: {situacoes[2]}")
print(f"Percentual de aprovados: {percentual_aprovados:.1f}%")
print(f"Médias em ordem decrescente: {sorted(medias, reverse=True)}")
# reverse=True imprime ao contrário
