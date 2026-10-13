# Estrutura: Lista. A Tupla e o Conjunto seriam opções inadequadas, pois a primeira não permite trocar a ordem
# nem substituir os elementos e o segundo não possui ordem definida nem aceita que tenham duplicadas.

playlist = ["Quando minha vida vai começar", "Como mel", "Saber quem eu sou",
             "Que mais vou fazer", "Família madrigal"]

while True:
    print("========== PLAYLIST COMPLETA ==========")

    if not playlist:
        print("Sua playlist está vazia!")

    else:
        for indice, musica in enumerate(playlist):
            print(f"{indice} : {musica}")

print("================================================")
           