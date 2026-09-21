palavra_correta = "sexta"

while True: # Se a condição é sempre verdadeira, ele roda.
    palavra = input("Palavra:")
    if palavra != palavra_correta:
        print("Errouuu!!! Tente novamente!")
    else:
        print("Acertou! Parabéns!")
        break # Para o módulo de repetição (sai do lup infinito) quando a pessoa acertar

print("Obrigado por participar.")