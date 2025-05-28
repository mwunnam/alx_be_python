task = input("Enter your task: ")
priority = input("(high, medium, low): ")
time_bound = input("yes or no")

match priority:
    case "high":
        if input == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that but not time bound at the moment!")

    case "medium":
        if input == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task do will to do in soon!")
        else:
             print(f"Reminder: '{task}' is a {priority} priority task but not time bound, you need to consider it later")
    case "low": 
        if input == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task do it later")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task delegate it!")
