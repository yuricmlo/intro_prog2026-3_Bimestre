print("Chegou o fim de semana! Vamos ver o seu nível de maratona de séries e animes.")

quantidade_de_horas = float(input("Digite a quantidade de horas que você passou assistindo:"))

if quantidade_de_horas < 1:
    print("Expectador casual.")
elif quantidade_de_horas <= 3:
    print("Maratonista iniciante.")
elif quantidade_de_horas < 3 or quantidade_de_horas <= 5:
    print("Maratonista profissional.")
else:
    print("Desligue a tela, seu viciado!")