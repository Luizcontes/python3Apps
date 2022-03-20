print("BANCO DINHEIRO CERTO\n")
print("Simulacao de emprestimo")
print("Qual e o seu rendimento mensal? ", end="")
rendimento = float(input())
print("qual e o montante que pretende pedir? ", end="")
montante = float(input())
print("\nO cliente tem um salario de %.2f euros e pretende um emprestimo de %.2f euros" % (rendimento, montante))
if (rendimento / montante) < 5:
    print("\nFinanciamento negado!!!")
else:
    print("\nFinanciamento concedido!!!")
print("\nObrigado por nos consultar")
