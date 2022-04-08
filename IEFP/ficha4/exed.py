print("Completando nomes")
print("Insira os seus primeiros 4 nomes")

nome = ""
for i in range(0,4):
    nome = nome + input("Nome: ") + " "
print("O seu nome completo e: ", nome)

print("Calculando a media do seu peso nos ultimos 3 meses (em kg)")
peso = 0
for z in range(0,3):
    peso = peso + int(input("Mes: "))
print("A media do seu peso nos ultimos 3 meses e de: ", peso/3)
a = input("Prima qualquer tecla para continuar...")