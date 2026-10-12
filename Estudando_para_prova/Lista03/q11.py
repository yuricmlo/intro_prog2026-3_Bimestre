ano = int(input("Digite o ano:"))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto, tivemos/teremos projeto especial!")

else:
    print("O ano não é bissexto, portanto não tivemos/teremos projeto especial.")