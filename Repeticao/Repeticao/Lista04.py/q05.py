# Algoritimo de Euclides (pesquisar) - máximo divisor comum (MDC)

numA = int(input("Número A:")) # Tem que ser sempre maior que o numero b
numB = int(input("Número B:"))
if numA < numB:
    numA, numB = numB, numA 

while numB != 0:
    resto = numA % numB
    numA = numB
    numB = resto

print(f"MDC = {numA}")

# Calcular o MMC(A, B) = (A * B) / MDC (A, B)