while True:
    try:
        num1 = int(input("Insert the first number: "))
        break
    except ValueError:
        print("Please insert a valid number!")
while True:
    while True:
        try:
            num2 = int(input("Insert the second number: "))
            break
        except ValueError:
            print("Please insert a valid number!")
    try:
        print(num1, "/", num2, "=", num1/num2)
        break
    except ZeroDivisionError:
        #pass
        print("Can`t divide by zero!")
print("Fim do programa!")