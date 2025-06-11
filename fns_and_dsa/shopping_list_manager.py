def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            if item == None:
                print("No Item entered")
                continue

            shopping_list.append(item)
            print(f"{item} added to shopping list\n")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item you want to remove: ")
            if item == None or item not in shopping_list:
                print("No Item entered or Item not found\n")
                continue

            else:
                print(f"{item} removed from shopping list\n")
                shopping_list.remove(item)


        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Your list is empty\n")
                continue

            for item in shopping_list:
                print(item)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
