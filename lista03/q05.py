n1 = int(input("Primeira nota:"))
n2 = int(input("Segunda nota:"))
media = n1 + n2 / 2
if media >= 60:
    print("Parabéns, você foi APROVADO! Você é foda!")
if media < 60 and media >= 20:
    print("Estude para a prova final, vamos à Igreja.")
if media < 20:
    print("REPROVADO direto! Digo é valha!")
