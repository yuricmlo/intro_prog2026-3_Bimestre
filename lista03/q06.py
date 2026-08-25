velocidade_veiculo = float(input("Velocidade do veículo em km/h:"))
if velocidade_veiculo <= 60:
    print("Velocidade permitida. Boa viagem!")
if velocidade_veiculo > 60 and velocidade_veiculo <= 70:
    print("Infração média!")
if velocidade_veiculo > 70:
    print("Infração gravíssima! Multa de R$ 293,47 e perda de pontos na CNH.")
                           
                           