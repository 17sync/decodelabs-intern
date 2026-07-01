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

## Project-2
This project is a command-line Expense Tracker. It enables users to record, categorize, and manage expenses while automatically calculating the total amount spent through an interactive menu-driven interface.

**- expense.py**
```py
expenses=[]

def addExpense(): pass
def viewExpenses(): pass
def viewTotal(): pass
def highestExpense(): pass
def deleteExpense(): pass

def menu():
    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Highest Expense")
        print("5. Delete Expense")
        print("6. Exit")

        operation=input("Choose an Operation: ")

        if operation=="1": addExpense()
        elif operation=="2": viewExpenses()
        elif operation=="3": viewTotal()
        elif operation=="4": highestExpense()
        elif operation=="5": deleteExpense()
        elif operation=="6":
            print("\nThank you for using my Expense Tracker!")
            break
        else:
            print("Invalid input, try again.\n")


def addExpense():
    try:
        amount=float(input("Enter expense amount: Rs. "))

        if amount<=0:
            print("Expense must be greater than 0.\n")
            return

        category = input("Enter category: ").strip()

        if category=="":
            category="General"

        expense={
            "amount": amount,
            "category": category
        }
        expenses.append(expense)

        print("Expense added successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")


def viewExpenses():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    print("\n====== EXPENSES ======")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index} | Rs. {expense['amount']:.2f} | {expense['category']}")


def viewTotal():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    total=0

    for expense in expenses:
        total+=expense["amount"]

    print(f"\nTotal Spent: Rs. {total:.2f}\n")


def highestExpense():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    highest=expenses[0]

    for expense in expenses:
        if expense["amount"]>highest["amount"]:
            highest=expense

    print("\nHighest Expense")
    print(f"Category: {highest['category']}")
    print(f"Amount: Rs. {highest['amount']:.2f}\n")


def deleteExpense():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    try:
        expenseNumber=int(input("Enter expense number to delete: "))

        if 1<=expenseNumber<=len(expenses):
            expenses.pop(expenseNumber-1)
            print("Expense deleted successfully.\n")
        else:
            print("Expense not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")


menu()
```

The project focuses on strengthening core Python concepts such as arithmetic operations, accumulators, lists, dictionaries, loops, functions, conditional statements, and input validation. It provides practical experience in processing numerical data and managing collections of information, serving as a foundation for building more advanced financial and backend applications.

## Project-3
A straightforward command-line Random Password Generator developed in Python as part of the DecodeLabs Python Development Internship. It allows users to generate secure, customizable passwords by specifying a desired length and optionally including special characters.

**- random.py**
```py
import random
import string


def generatePassword(): pass
def menu(): pass


def menu():
    while True:
        print("\n===== RANDOM PASSWORD GENERATOR =====")
        print("1. Generate Password")
        print("2. Exit")

        operation=input("Choose an Operation: ")

        if operation=="1":
            generatePassword()

        elif operation=="2":
            print("\nThank you for using my Password Generator!")
            break

        else:
            print("Invalid input, try again.\n")


def generatePassword():
    try:
        length=int(input("Enter password length: "))

        if length<4:
            print("Password length must be at least 4.\n")
            return

        useSpecial=input("Include special characters? (Y/N): ").strip().lower()
        characters=string.ascii_letters+string.digits

        if useSpecial=="y":
            characters+=string.punctuation

        password=[
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits)
        ]

        if useSpecial=="y" or useSpecial=="Y":
            password.append(random.choice(string.punctuation))

        while len(password)<length:
            password.append(random.choice(characters))
        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))
        print()

    except ValueError:
        print("Please enter a valid number.\n")


menu()
```

The project focuses on strengthening core Python concepts such as module integration, string manipulation, loops, conditional statements, functions, and input validation. By utilizing Python's built-in random and string libraries, it demonstrates how standard libraries can be leveraged to create practical security-focused utilities while reinforcing the fundamentals of automation and secure data generation.

## Project-4
 A command-line General Knowledge Quiz. It presents users with a series of multiple-choice questions, evaluates their responses, and displays a final score upon completion through a simple interactive interface.

**- quiz.py**
```py
score=0

def startQuiz(): pass
def showScore(): pass
def menu(): pass


def menu():
    while True:
        print("\n========== GENERAL KNOWLEDGE QUIZ ==========")
        print("1. Start Quiz")
        print("2. Exit")

        operation=input("Choose an Operation: ")
        if operation=="1":
            startQuiz()
        elif operation=="2":
            print("\nThank you for playing!")
            break
        else:
            print("Invalid input, try again.\n")


def startQuiz():
    global score
    score=0

    questions=[
        {
            "question":"1. What is the capital of Pakistan?",
            "options":["A. Lahore", "B. Karachi", "C. Islamabad", "D. Peshawar"],
            "answer":"C"
        },
        {
            "question":"2. Which planet is known as the Red Planet?",
            "options":["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer":"B"
        },
        {
            "question":"3. How many continents are there?",
            "options":["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer":"C"
        },
        {
            "question":"4. Which language is primarily used for web page styling?",
            "options":["A. HTML", "B. Python", "C. CSS", "D. Java"],
            "answer":"C"
        },
        {
            "question":"5. What is 15 x 4?",
            "options":["A. 60", "B. 45", "C. 50", "D. 65"],
            "answer":"A"
        }
    ]

    for question in questions:
        print("\n"+question["question"])

        for option in question["options"]:
            print(option)

        answer=input("Your Answer: ").strip().lower()

        if answer==question["answer"]:
            print("Correct!\n")
            score+=1
        else:
            print("Wrong!\n")

    showScore()


def showScore():
    print("\n========== QUIZ COMPLETE ==========")
    print(f"Final Score: {score}/5")

    if score==5:
        print("Outstanding! Perfect score!\n")
    elif score>=3:
        print("Well done!\n")
    else:
        print("Keep practicing!\n")

menu()
```

 The project reinforces fundamental Python concepts such as conditional statements, loops, functions, lists, dictionaries, variables, and input handling. It provides practical experience in implementing program logic, validating user input, and managing application flow, serving as a foundation for building more interactive console-based applications.
