import time

print("Aplicacao que descomplica a tabuada")
print("___________________________________\n")
tabuada = int(input("Qual e a tabuada que considera mais dificil? "))
print("Vamos, entao, a isso... bem devagar...")
for x in range(1,11):
    print("\t",tabuada," x ", x, " = ", tabuada * x)
    time.sleep(2)
z = int(input("\nPrima qualquer tecla para continuar..."))

