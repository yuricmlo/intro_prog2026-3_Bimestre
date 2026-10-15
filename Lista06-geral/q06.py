# Estrutura: conjunto, pois não aceita elementos repetidos e 
# um elemento pode estar em 2 conjuntos diferentes 

programacao = {"Yuri", "Lara","Júlia","Kaio","João","Nicholas"}
robotica = {"Nicholas","João","Davi Lucas","Lívia"}

print(f"Clube de Programação: {programacao}")
print(f"Clube de Robótica: {robotica}")

print(f"Alunos que participam dos dois clubes: {programacao & robotica}")
print(f"Alunos que participam de pelos menos um dos clubes: {programacao | robotica}")
print(f"Alunos que participam de somente um dos clubes: {programacao ^ robotica} ")
print(f"Alunos exclusivos da Robótica: {robotica - programacao}")
