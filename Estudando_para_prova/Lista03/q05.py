nota1 = float(input("Digite a nota do 1º semestre:"))
nota2 = float(input("Digite a nota do 2º semestre:"))

media_das_notas = nota1 + nota2 / 2

if media_das_notas >= 60:
    print("Parabéns, você foi APROVADO(A)!")
    print(f"Média total: {media_das_notas:.0f}")
if media_das_notas < 60 and media_das_notas >= 20:
    print("Você ficou em RECUPERAÇÃO!")
    print(f"Média total: {media_das_notas:.0f}")
if media_das_notas < 20:
    print("Você foi REPROVADO(A)!")
    print(f"Média total: {media_das_notas:.0f}")