# Comando for
texto = "Três pratos de Trigo para três Tigres tristes"
vogais = "AEIOU"
n = 0 # Se a letra for uma vogal, contará +1
#in: Operação de conjuntos (pertence, não pertence)
# .upper() Transforma o caractere em maiúsculo, como Python diferencia letras maiúscula de minúsculas, temos que converter tudo para mai. ou minu.
# .lower() transforma tudo em minúsculo
# Se tiver uma letra com acento gráfico, deve-se adicionar ao conjunto. Ex: vogais = "AEIOUÁÃÂÉÊÍÓÔÕÚ"
for letra in texto:
    if letra.upper() in vogais:
        n = n + 1
print(f"Vogais: {n}")