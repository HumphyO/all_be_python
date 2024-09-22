Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
        case "high":
            Reminder = f"Reminder: {Task} has HIGH priority!"
        case "medium":
            Reminder = f"Reminder: {Task} has MEDIUM priority."
        case "low":
            Reminder = f"Reminder: {Task} has LOW priority."
        case _:
            Reminder = f"Reminder: {Task} has UNKNOWN priority."

if Time_Bound == "yes":
        Reminder += "This task requires immediate attention today!"
        print(Reminder)
else:
     print('Note, this task can be done later!')
