tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#As a user, to manage my task list I would like a program that allows me to:

#1. Print a list of uncompleted tasks
def print_uncompleted_tasks(tasklist):
    uncompleted_tasks = []
    for task in tasklist:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    print(uncompleted_tasks)
    return uncompleted_tasks


print_uncompleted_tasks(tasks)
print("-----------------------")

#2. Print a list of completed tasks
def print_completed_tasks(tasklist):
    completed_tasks = []
    for task in tasklist:
        if task["completed"] == True:
            completed_tasks.append(task)
    print(completed_tasks)
    return completed_tasks


print_completed_tasks(tasks)
print("-----------------------")

#3. Print a list of all task descriptions
def print_all_task_descriptions(tasklist):
    task_descriptions = []
    for task in tasklist:
        task_descriptions.append(task["description"])
    return task_descriptions


print(print_all_task_descriptions(tasks))
print("-----------------------")

#4. Print a list of tasks where time_taken is at least a given time

#5. Print any task with a given description