valor = float(input("Valor da Conta:"))
pessoas = int(input("Quantidade de pessoas:"))
taxa = input("Adicionar 10% (s ou n):")

if taxa == "s":
    valor = valor + valor * 0.10 # 10% = 0.10
elif taxa =="n":
    print("Sem taxa de 10%")
else:
    print("Opção inválida! Desconsiderar tava")
valor_por_pessoa = valor / pessoas

print("===== Resumo da Conta =====") # Enfeite
print(f"Valor da conta = R$ {valor:.2f}")
print(f"Valor por pessoa = R$ {valor_por_pessoa:.2f}")


