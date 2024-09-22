Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
        case "high":
            reminder = "This is a high-priority task!"
        case "medium":
            reminder = "This is a medium-priority task."
        case "low":
            reminder = "This is a low-priority task"
        case _:
            reminder = "Invalid level of Priority"

if Time_Bound == "yes":
        reminder += "This task requires immediate attention today!"
        print(f"Reminder: {Task} - {reminder}")
else:
     reminder += "This activity can be carried out later!"
     print(f"Note: {Task} - {reminder}")


