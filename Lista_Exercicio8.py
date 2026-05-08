quadrados = list()

for numero in range(1,11):
    quadrados.append(numero ** 2)

soma = sum(quadrados)

print(quadrados)
print(f"Soma: {soma}")