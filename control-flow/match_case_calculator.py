num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print("The result is: {}".format(num1 + num2))
    case "-":
        print("The result is: {}".format(num1 - num2))
    case "*":
        print("The result is {}".format(num1 * num2))
    case "/":
        if numb2 != 0:
            print("The result is: {}".format(num1 / 0))
        else:
            print("You can not divide by zero")
    case _:
        print("Invalide operation.")