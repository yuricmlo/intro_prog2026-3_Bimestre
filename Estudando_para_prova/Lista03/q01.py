valor = float(input("Qual o valor total da conta a pagar?"))
pessoas = int(input("Qual a quantidade de pessoas?"))
taxa = input("Quer adicionar a taxa de 10% do saimon, nosso garçom? (s ou n)")

if taxa == "s":
    valor = valor + valor * 0.1
elif taxa == "n":
    print("Sem taxa.")
else:
    print("Como você não respondeu (s ou n) iremos desconsiderar a taxa do saimon.")

valor_por_pessoa = valor / pessoas

print(">>> Resumo da Conta")
print(f"=> Valor total: {valor:.2f}")
print(f"=> Valor individual: {valor_por_pessoa:.2f}")
print("Obrigado pela preferência, querido(a)!")