task = input('Enter task description: ')
priority = input('choose priority (high, medium, low): ')
time_bound = input('Is the task time bound (yes/no): ')

match priority:
        case "high":
            reminder = f"Task: {task} has HIGH priority!"
        case "medium":
            reminder = f"Task: {task} has MEDIUM priority."
        case "low":
            reminder = f"Task: {task} has LOW priority."
        case _:
            reminder = f"Task: {task} has UNKNOWN priority."

if time_bound == "yes":
        print(" This task requires immediate attention today!")
else:
     print("This task canbe done in a different time!")
