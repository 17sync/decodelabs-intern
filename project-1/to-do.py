tasks=[]
nextID=1

def addTask(): pass
def viewTasks(): pass
def markComplete(): pass
def deleteTask(): pass

def menu():
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        operation=input("Choose an Operation: ")

        if operation=="1": addTask()
        elif operation=="2": viewTasks()
        elif operation=="3": markComplete()
        elif operation=="4": deleteTask()
        elif operation=="5":
            print("\nThank you for using my To-Do List!")
            break
        else: print("Invalid input, try again.\n")

def addTask():
    global nextID

    taskTitle=input("Enter task: ").strip()
    if taskTitle=="":
        print("Task cannot be empty!\n")
        return

    task={
        "id":nextID,
        "title":taskTitle,
        "completed": False
    }

    tasks.append(task)
    nextID+=1

    print("Task added successfully!\n")


def viewTasks():
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n====== TO-DO LIST ======")

    for task in tasks:
        status="✓"if task["completed"] else "✗"
        print(f'{task["id"]} | {task["title"]} {status}')

def markComplete():
    if not tasks:
        print("No tasks available.\n")
        return

    try:
        taskID=int(input("Enter task ID: "))

        for task in tasks:
            if task["id"]==taskID:
                task["completed"]=True
                print("Task marked as completed.\n")
                return

        print("Task ID not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def deleteTask():
    if not tasks:
        print("No tasks available.\n")
        return

    try:
        taskID=int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"]==taskID:
                tasks.remove(task)
                print("Task deleted successfully.\n")
                return

        print("Task ID not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")


menu()