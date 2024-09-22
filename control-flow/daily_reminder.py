Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
        case "high":
            reminder = f"Reminder: {Task} has HIGH priority!"
        case "medium":
            reminder = f"Reminder: {Task} has MEDIUM priority."
        case "low":
            reminder = f"Reminder: {Task} has LOW priority."
        case _:
            reminder = f"Reminder: {Task} has UNKNOWN priority."

if Time_Bound == "yes":
        reminder += "This task requires immediate attention today!"
        print(reminder)
else:
     print('Note, this task can be done later!')
