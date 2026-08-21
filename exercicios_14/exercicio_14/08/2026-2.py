# Média no padrão 0 a 100
media = int(input("Média do aluno(a):"))
# Testar se a média é maior ou igual a 60
if media >= 60:
    print("Aluno aprovado!")
# Testar se além de ser menor que 60, é maior que 30
elif media >= 30:
    print("Aluno em recuperação.")
# Senão, usamos elif para dizer que as duas condicões é falsa e o auluno está reprovado
else:
    print("Aluno reprovado, gamer over!")    