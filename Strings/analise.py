# Analise de Log

arquivo = open("log_acessos_1000_registros.txt", "r",
               encoding="utf-8")

#print(arquivo.read())
falhas = []
usr_falha = set()
for linha in arquivo:
    if "FALHA" in linha:
        falhas.append(linha)
        ocorrencia = linha.split(" ")
        usuario = ocorrencia[3].split("=")
        usr_falha.add(usuario[1])

#print(*falhas)
print(f"Total de falhas = {len(falhas)}")
print(usr_falha)