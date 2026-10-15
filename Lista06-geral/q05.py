# Estrutura: depois de ser criada a sequência da tupla não poder ser alterada

cor1 = int(input("Digite a 1ª cor:"))
cor2 = int(input("Digite a 2ª cor:"))
cor3 = int(input("Digite a 3ª cor:"))

if (cor1 < 0 or cor1 > 255) or (cor2 < 0 or cor2 > 255) or (cor3 < 0 or cor3 > 255):
    print("Erro: as cores devem estar entre 0 e 255!")

else:

    cores = (cor1, cor2, cor3)

    vermelho, verde, azul = cores

    print(f"RGB{vermelho, verde, azul}")