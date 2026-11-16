eventos = [4,4,4,2,2,8,8,8,8,3]

codigos = []
quantidades = []

cod_atual = eventos[0] # Ou seja, o código atual é 4
contador = 1 

for i in range(1, len(eventos)):
    if eventos[i] == cod_atual:
        contador += 1

    else:
        codigos.append(cod_atual)
        quantidades.append(contador)
        cod_atual = eventos[i]
        contador = 1


codigos.append(cod_atual)
quantidades.append(contador)

indice_maior = quantidades.index(max(quantidades))


print("====== RESUMO ======")
print(f"Eventos registrados - {eventos}")
print(f"Códigos - {codigos}")
print(f"Quantidades - {quantidades}")
print(f"1º código de maior ocorrência consecutiva - {codigos[indice_maior]}")