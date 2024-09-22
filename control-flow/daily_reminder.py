Task = input("Enter your task: ")
Priority = input("What priority does it take? (high/medium/low): ")
Time_Bound = input("Is it time bound? (yes/no): ")

def process_task(task, priority, time_bound):
    reminder = ""

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
     print('Note, this task can be done later!')

