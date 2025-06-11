#!/usr/bin/python3.10

shopping_list = []

while True:
    print("\nMenu")
    print(f"1. To add an item \n2. To remove Item\n3. To view List\n4. Exit")
    user_input = input("What would you like to do: ")

    match user_input:
        case "1":
            item = input("Enter Item to add: ")
            shopping_list.append(item)

        case "2":
            item = input("Enter Item you want to remove: ")
            if input not in shopping_list:
                print(f"{item} not found in your shopping list")
                continue

            shopping_list.remove(item)

        case "3":
            for x in shopping_list:
                print(x)

            print()

        case "4":
            break

        case _:
            print("Invalid input")

