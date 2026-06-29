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