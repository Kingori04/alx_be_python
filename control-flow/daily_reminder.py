def main():
    # Prompt for the task description, priority, and time sensitivity
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use a Match Case statement to process the priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level."

    # If the task is time-bound, update the reminder
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the customized reminder
    print("\nReminder:", reminder)

# Call the main function to run the program
if __name__ == "__main__":
    main()

