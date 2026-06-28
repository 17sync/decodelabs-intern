# Overview
This repositry contains the projects I coded during my Python Development Internship at Decode Labs. These 4 hands-on projects helped me strengthen my understanding of Python programming and software development practices as a whole.

## Project-1
A simple command-line based To-Do List application. It demonstrates fundamental programming concepts by allowing users to create, view, update, and delete tasks through a simple interactive interface.

**- to-do.py**
```py
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
```

The project emphasizes the practical use of Python data structures, particularly lists and dictionaries, while reinforcing concepts such as functions, loops, conditional statements, input validation, and modular programming. It serves as an introduction to managing structured data in memory, laying the foundation for more advanced backend and data management applications.