pares = 0

for cont in range(5):
    num = int(input("Digite um número:"))
    if num % 2 == 0:
        pares = pares + 1

print(f"Você encontrou {pares} números pares.")