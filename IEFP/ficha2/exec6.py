nome = input("Insira o nome do aluno: ")
alNumero = int(input("Insira o numero do aluno: "))
cog = int(input("Avaliacao cognitica: "))
atVal = int(input("Avaliacao de Atitudes e Valores: "))

notaFinal = float(cog + atVal)

if notaFinal < 9.5:
    avalQual = "Insatisfatorio"
elif notaFinal < 13.6:
    avalQual = "Satisfatorio"
elif notaFinal < 15.6:
    avalQual = "Muito Satisfatorio"
elif notaFinal < 18.1:
    avalQual = "Bom"
else:
    avalQual = "Excelente"

print("NOME\tNUMERO\tN FINAL\tAVALIACAO QUALITATIVA")
print("%s\t%s\t%2.1f\t%s" %(nome, alNumero, notaFinal, avalQual))
