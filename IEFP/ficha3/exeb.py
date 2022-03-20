i = 10
pares = 0
impares = 0
while i < 201:
    if i % 2 == 0:
        pares = pares + i
    else:
        impares = impares + i
    i = i + 1
print("A soma dos numeros pares entre 10 e 200 e: ", pares)
print("A soma dos numeros impares entre 10 e 200 e: ", impares)
