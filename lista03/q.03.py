quantidade_de_horas = float(input("Quantidade de horas por dia:"))
if quantidade_de_horas <= 1:
    print("Expectador casual.")
elif quantidade_de_horas <= 3:
    print("Maratonista iniciante.")
elif quantidade_de_horas <= 5:
    print("Maratonista profissional")
else: 
    print("Alerta vermelho! Vá ver o Sol!")
