mensagem = input("Mensagem: ")
tamanho = len(mensagem) # len: função para contar quantos caracteres tem uma string
if tamanho < 3 or tamanho > 140:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
    print("Mensagem enviada com sucesso!")