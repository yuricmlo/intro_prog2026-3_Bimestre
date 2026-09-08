paisA = 80000
paisB = 200000
anos = 0
while paisA < paisB: # Vou simular o crescimento da população enquanto a população do país A for menor que a do país B.
    paisA += paisA * 0.03 # i = i+1
    paisB += paisB * 0.015 # i = i+1
    anos += 1
print(f"País A superou o País B em {anos} anos.")
print(f"País A: {paisA:.0f} habitantes.")
print(f"País B: {paisB:.0f} habitantes.")



