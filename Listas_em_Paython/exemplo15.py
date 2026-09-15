import random # Biblioteca como nome aleatório

lista = []
while True:
    nome =  input("Nome para o sorteio:")
    if nome == "":
        break
    else: 
        lista.append(nome)
print(lista)
random(lista)
ganhador = random.choice(lista)
print(f"Ganhador da moto: {ganhador}")