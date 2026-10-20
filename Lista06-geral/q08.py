# Lista, pois é ordenada e  aceita repetições.

historico_temperaturas = []

for i in range(0, 12):
    temperatura = float(input("Digite a temperatura registrada neste momento:"))
    historico_temperaturas.append(temperatura)

print(f"Média das temperaturas: {sum(historico_temperaturas) / len(historico_temperaturas)}°C")
print(f"Maior temperatura: {max(historico_temperaturas)}°C")
print(f"Posição da primeira ocorrência da maior temperatura: {historico_temperaturas.index(max(historico_temperaturas))}")

media_das_temperaturas = sum(historico_temperaturas) / len(historico_temperaturas)

num_temperaturas_acima_media = 0

for temp in historico_temperaturas: 
    if temp > media_das_temperaturas:
        num_temperaturas_acima_media += 1
        
print(f"Leituras acima da média: {num_temperaturas_acima_media}")