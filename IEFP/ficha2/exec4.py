# -*- coding: utf-8 -*-

print("Menu das Conversoes:")
print("1 - Decimal -> Binario")
print("2 - Binario -> Decimal")
print("3 - Decimal -> Octal")
print("4 - Decimal -> Hexadecimal\n")
op=int(input("Qual a operacao pretendida: "))

if (op==1):                                                                 # condicional if
    decimal=int(input("Introduza o numero decimal: "))
    print("Decimal %d = Binario %s" %(decimal,bin(decimal)))                # bin(decimal) -> converte decimal para binario
    print("{0:b}".format(decimal))                                          # {0:b} -> formatacao de texto pra exibir o decimal em binario
elif (op==2):
    binario=input("Introduza um valor binario, com o formato '0b...': ")      
    print("Binario %s = Decimal %s" %(binario,int(binario,2)))              # int(binario,2) -> converte de binario para decimal
elif (op==3):                       
    decimal=int(input("Introduza o numero decimal: "))
    print("Decimal %d = Octal %s" %(decimal,oct(decimal)))                  # oct(decimal) -> coverte de decimal para octal
    print("{0:o}".format(decimal))                                          # {0:b} -> formatacao de texto pra exibir o decimal em octal
else:
    decimal=int(input("Introduza o numero decimal: "))
    print("Decimal %d = Hexadecimal %s" %(decimal,hex(decimal)))            # hex(decimal) -> converte de hexadecimal para decimal
    print("{0:x}".format(decimal))                                          # {0:b} -> formatacao de texto pra exibir o decimal em hexadecimal
