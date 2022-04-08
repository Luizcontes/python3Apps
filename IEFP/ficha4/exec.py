print("Insira 3 nomes e descubra o maior")

nome = []
idade = []
media = 0
maiorN = ""

for i in range(0,3):
    nome.append(input("Nome: "))
    idade.append(input("\tIdade: "))
    if(len(nome[i]) > len(maiorN)):
        maiorN = nome[i]
    media = media + int(idade[i])
media = media / len(nome)

print("Maior nome e: ", maiorN)
print("Media das idades e: ", media)
a = input("Prima qualquer tecla para continuar...")
