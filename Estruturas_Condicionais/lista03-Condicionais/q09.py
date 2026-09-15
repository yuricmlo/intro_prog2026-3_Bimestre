idade = int(input("Idade:"))
carteira =  input("Carteira de estudante (s/n):")
if idade >= 60:
    print("Gratuitidade concedida por Lei!")
elif idade < 18 or carteira == "s":
    print("Meia entrada autorizada!")
else:
    print("Passagem completa: R$ 1.50")