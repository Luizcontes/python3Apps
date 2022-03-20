peso = int(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

IMC = peso / (altura*altura)

print("Seu IMC e: %2.2f" %(IMC))
print("Indice considerado:")

if IMC < 16:
    print("Magreza grave")
elif IMC < 17:
    print("Magreza moderada")
elif IMC < 18.5:
    print("Magreza leve")
elif IMC < 25:
    print("Saudavel")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Obesidade Grau 1")
elif IMC < 40:
    print("Obesidade Grau 2 (severa)")
else:
    print("Obesidade Grau 3 (morbida)")