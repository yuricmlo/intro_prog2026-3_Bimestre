conta = int(input("Valor da conta:"))
pago = int(input("Valor do pagamento:"))
troco = pago - conta
print(f"Troco: R$ {troco:.2f}")

# - 1 de 50,00
# - 2 de 20,00
# - 0 de 10,00
# - 1 de 5,00
# - 1 de 2,00

notas = [50,20,10,5,2,1]
for nota in notas:
    num_notas = troco // nota
    if num_notas != 0:
        print(f">> {num_notas} de {nota:.2f}")
    troco = troco % nota # É para atualizar o troco e repetir o loop
