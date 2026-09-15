nomes = ["Maria","João","José","Rosa"]
print(f"Nomes: {nomes}")
while True: # Significa que é um loop infinito
    nome = input("Nome para adicionar:")
    if nome == "": # No caso, esse vazio seria o "enter" quando a genta aperta para sair
        break
    else:
        if nome not in nomes: # Se nome não pertence a nomes, "adicione".
            nomes.append(nome)
        print(f"Nomes: {nomes}")

# Usamos .append() para inserir um item no final da lista 