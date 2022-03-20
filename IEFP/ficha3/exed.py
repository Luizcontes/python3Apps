import random

guess = 0
ale = random.randint(1, 20)
i = 0
while guess != ale:
    guess = int(input("Adivinha um numero de 1 a 20: "))
    if guess > ale:
        print("O numero que introduziu e maior")
    else:
        print("O numero que introduziu e menor")
    i = i +1
    print("")
print("O numero a adivinhar era", ale)
print("Parabens, adivinhaste o numero correto em", i, "tentativas.")