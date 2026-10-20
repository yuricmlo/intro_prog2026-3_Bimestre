# Seria melhor combinar a duas estruturas, pois a lista é ordenada e o conjunto 
# não aceitas repeticões.

historico = []

numero_de_escaneamentos = int(input("Digite quantos códigos quer escanear:"))

for i in range(numero_de_escaneamentos):
    codigo = int(input("Digite o código do produto:"))
    historico.append(codigo)

print("=> Sequência de leituras:")
print(historico)

print("=> Quantidade de códigos diferentes:")
print(f"{len(set(historico))}")

print("=> Versão em ordem crescente:")
print(f"{sorted(set(historico))}")
