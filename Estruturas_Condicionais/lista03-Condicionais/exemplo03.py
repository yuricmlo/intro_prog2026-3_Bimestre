valor = -1 # pode ser qualquer valor diferente de zero para que habilite a entrada do lup (while)
soma = 0
while valor != 0:
    valor = int(input("Digite um número:"))
    soma = soma + valor
print(f"A soma dos números é {soma}.")