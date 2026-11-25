# Analise de Log

arquivo = open("log_acessos_1000_registros.txt", "r",
               encoding="utf-8")

print(arquivo.read()) 
#falhas = []
#usr_falha = set()
#for linha in arquivo:
#    if "FALHA" in linha:
#       falhas.append(linha) # Adiciona a linha à lista falhas
#        ocorrencia = linha.split(" ") # Toda vez que encontra um espaço na linha, faz um fatiamento
#        usuario = ocorrencia[3].split("=") # Pega o índece 3 desse anterior fatiamento e fatia ele 
#        usr_falha.add(usuario[1]) # Pega o índice 1 do fatiamento anterior e adiciona-o no conjunto usr_falha

#print(*falhas) #- Imprime cada linha do conjunto sem está separada por vírgula (linha por linha)
#print(f"Total de falhas = {len(falhas)}")
#print(f"Usuários que acessaram o sistema {usr_falha}")

# Adicionamos a linha que possuí "FALHA" à lista falhas para, no final imprimirmos a quantidade total de 
# falhas.
# Fatiamos cada linha para conseguirmos acessar o nome do usuário e adicionar ao conjunto "usr_falha" para
# registrarmos os usuários cujos acessos falharam sem que fiquemos com usuários repetidos.