import time, os

print("A media da turma, no 1º modulo de PSI\n\n")
os.system('color F2')
time.sleep(2)

nome = [] 
nota = []

for i in range(0,3):
    print("\nAluno nº", i+1," :")
    print("-----------\n")
    nome.append(input("\t\tNome? "))
    nota.append(int(input("\t\tNota do 1º modulo de PSI: ")))

media = 0
for a in range(0,3):
    media = media + nota[a]

print("\n\nA media da turma, no 1º modulo de PSI e de\n")
time.sleep(5)
print("\tAguarde...")
time.sleep(5)
print("\tAguarde mais um pouco...")
time.sleep(10)
print("Agora, sim! A resposta e...")
print(media/len(nota))

z = input("\nPrima qualquer tecla para continuar...")