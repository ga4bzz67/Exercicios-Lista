numeros = list(range(1,101))
num_pares = list()

for numero in numeros:
    if numero % 2 == 0:
        num_pares.append(numero)
print(num_pares)