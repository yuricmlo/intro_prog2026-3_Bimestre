# Estrutura: Conjunto, pois consegurá filtrar os nomes repetidos

quant_inscricoes = ["José", "Inácio", "Rosa", "José", "Maria",
         "Maria", "Maria", "José", "Carlos", "Alex"]

num_inscritos = set(quant_inscricoes)

print(f"Quantidade de inscrições feitas: {len(quant_inscricoes)}.")
print(f"Quantidade de pessoas inscritas de fato: {len(num_inscritos)}.")
print(f"Nomes em ordem alfabética: {sorted(num_inscritos)}.")