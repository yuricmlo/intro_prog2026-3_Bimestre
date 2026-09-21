ano = int(input("Ano para projeto especial:"))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto, teremos Projeto Especial!")
if ano <= 2026:
    print("Oh, que pena. Esse ano já passou!")
else:
    print("Não teremos Projeto Esepecial")