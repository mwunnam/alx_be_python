task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that but not time bound at the moment!")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task do will to do in soon!")
        else:
             print(f"Reminder: '{task}' is a {priority} priority task but not time bound, you need to consider it later")
    case "low": 
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task do it later")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task delegate it!")
