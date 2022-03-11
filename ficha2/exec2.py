print("***VALIDADOR DE IDADE PARA CARTA DE CONDUCAO\n")
print("Insira sua idade")
idade = input()
if int(idade) < 18:
    print("Ainda lhe falta", 18 - int(idade), "anos para poder tirar a carta de conducao")
elif int(idade) < 80:
    print("Pode renovar sua carta sem problemas")
else:
    print("Desculpe-me mas sua idade ja nao permite renovacao da carta de conducao")
    
    