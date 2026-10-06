# Usamos chaves para fazer conjuntos e a ordem dos 
# elementos não importa e não tem elementos repetidos 

linguagens = {"python", "java", "c", 
              "java", "c", "python"}
print(linguagens)
print(f"cobol -> {"cobol" in linguagens}")

letras = set("python")
print(letras)
numeros = set([1, 2, 3, 4, 1, 3, 2])
print(numeros)