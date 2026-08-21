n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))

if n1 > n2:
    print(f"{n1} é maior ou igual {n2}")
elif n1 < n2:
    print(f"{n1} é menor que {n2}")
else:
    print(f"{n1} é igual a {n2}")