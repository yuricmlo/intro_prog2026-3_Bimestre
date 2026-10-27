# Estrutura: Conjuntos (sem repetição de elementos)

alunos_manha = set()
alunos_tarde = set()
n_manha = int(input("Quantidade de acessos pela manhã:"))
for i in range(n_manha):
    matricula = input("Matrícula:")
    alunos_manha.append(matricula)
n_tarde = int(input("Quantidade de acessos pela tarde:"))
for i in range(n_tarde):
    matricula = input("Matrícula:")
    alunos_tarde.append(matricula)

print(f"Acesso pela manhã: {alunos_manha}")
print(f"Acessos pela tarde: {alunos_tarde}")
print(f"Acessos nos dois turnos: {alunos_manha & alunos_tarde}")
print(f"Acessos somente pela manhã: {alunos_manha - alunos_tarde}")
print(f"Acessos somente à tarde: {alunos_tarde - alunos_manha}")
print(f"N° de acessos duante o dia: {alunos_manha ^ alunos_tarde}")