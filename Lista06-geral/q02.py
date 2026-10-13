# Estrutura: Tpula, pois mantém a posição e é possível desempacotar os índices

x = float(input("Digite o valor da posição x:"))
y = float(input("Digite o valor da posição y:"))

posic_inicial = (x, y)

# Desempacotar
x, y = posic_inicial 

if x > 0 and y > 0:
    print("1º Quadrante.")

elif x < 0 and y > 0:
    print("2º Quadrante.")

elif x < 0 and y < 0:
    print("3º Quadrante.")

elif x > 0 and y < 0:
    print("4º Quadrante.")

else:
    print("Ponto de origem.")