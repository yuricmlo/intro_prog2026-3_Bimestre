texto = len(input("Digite seu texto:"))
if texto < 3:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
if texto > 140:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
    print("Mensagem enviada com sucesso!")