lista_convidados = ["Yuri", "July", "Brian", "Carmen", "Spear", "Mariano", "Santiago", "Fábio", "Heithor"
                    , "Isabella", "Mirabel", "Dolores", "Julieta", "Pepa", "Luíza", "Abuela", "Bruno", "Casita" ]

nome_buscar = input("Digite seu nome e veja se ele está na lista de convidados:")

while nome_buscar not in lista_convidados:
    print(f"Nome: {nome_buscar}. Não localizado!")
    break