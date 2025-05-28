num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == '+':
    result = float(num1) + num2
    
print("The result is {:.0f}".format(result))