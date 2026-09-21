saldo = float(input("Saldo de moedas:"))
valor_skin = float(input("Valor da skin:"))

if saldo >= valor_skin:
    print("Compra realizada! Aproveite sua nova skin>")
    saldo = saldo - valor_skin
    print(f"Saldo restante R$ {saldo:.2f}")
else:
    print("Saldo insuficiente!")
    restante = valor_skin - saldo
    print(F"Saldo insuficiente! Faltam {restante} moedas para você comprar este item. Vá estudar e para de jogar Free Fire.")