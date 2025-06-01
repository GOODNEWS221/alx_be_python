task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()



match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a high priority task. Try to complete it soon."
    case "medium":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a medium priority task. Schedule it appropriately."
    case "low":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Note: '{task}' has an unknown priority. Please double-check your input."


print()
print(message)

