# Tabuada

#n = int(input("Número para gerar tabuada:")) uma tabuada por vez informando o número.
for n in range(11):
    for i in range(11):
        print(f"{n} x {i} = {n * i}")
    print() #Para não ficar tudo junto.