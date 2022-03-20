print("***IDENTIFICADOR DE TRIANGULOS\n")
numeros = [None] * 3
valCorr = 1
erroMsg = "A soma de dois lados qualquer nao pode ser menor que o terceiro lado, insira os valores novamente"
while valCorr == 1:
    for x in range(0, 3):
        print("Insira o valor do #"+ str(x+1), "lado ", end="")
        numeros[x] = int(input())
    if numeros[0] > numeros[1] + numeros[2]:
        print(erroMsg)
    elif numeros[1] > numeros[0] + numeros[2]:
        print(erroMsg)
    elif numeros[2] > numeros[0] + numeros[1]:
        print(erroMsg)
    else:
        valCorr = 0
if numeros[0] == numeros[1] == numeros[2]:
    print("\nEste triangulo e equilatero")
elif numeros[0] == numeros[1] or numeros[0] == numeros[2] or numeros[1] == numeros[2]:
    print("\nEste triangulo e isosceles")
else:
    print("\nEste triangulo e escaleno")
print("\nTchauuuuu!!!! :)")
