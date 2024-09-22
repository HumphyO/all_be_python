Task = input('Enter your task: ')
Priority = input('choose priority (high/medium/low): ')
Time_Bound = input('Is the task time bound (yes/no): ')

match Priority:
        case "high":
            reminder = f"Task: {Task} has HIGH priority!"
        case "medium":
            reminder = f"Task: {Task} has MEDIUM priority."
        case "low":
            reminder = f"Task: {Task} has LOW priority."
        case _:
            reminder = f"Task: {Task} has UNKNOWN priority."

if Time_Bound == "yes":
        print(" This task requires immediate attention today!")
else:
     print("This task canbe done in a different time!"))
