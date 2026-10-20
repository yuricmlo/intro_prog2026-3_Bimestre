# Estruturas: Tupla, pois cada assento é fixo e não pode ser alterado e conjunto porque não aceita elementos 
# repetidos evitando que seja reservado mais de uma vez

reservas = set()

while True:
    fila = int(input("Digite o número da fila:"))

    if fila == 0:
        break

    if fila != 0:
        coluna = int(input("Digite o número da coluna:"))
        assento = (fila, coluna)
    if assento in reservas:
                print("Erro! Esse assento já foi reservado.")

    else:
            reservas.add(assento)

print(f"Quantidade de assentos reservados: {len(reservas)}")

print("Assentos reservados em ordem:")

for assento in sorted(reservas):
     print(f"Fila: {assento[0]}, Coluna : {assento[1]}")
