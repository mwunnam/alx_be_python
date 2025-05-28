number = int(input("Enter the size of the patten: "))

row = 0
while row < number:
    for x in range(number):
        print("*", end="")
    print()
    row += 1