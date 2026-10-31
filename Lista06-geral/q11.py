# Estruturas: Lista, pois pode sofrer alterações na coleta e Tupla, pois não pode ser alterada depois da criação´
#o que ajuda a fazer um relatório fechado.

coleta_dados = []

for i in range(1, 7):
    resultado = input(f"Como foi o resultado {i} (ok ou falha)?")
    while resultado != "ok" and resultado != "falha":
            print("Erro! Informe ok ou falha.")
            break

    coleta_dados.append(resultado)

# Questão incompleta!

    







