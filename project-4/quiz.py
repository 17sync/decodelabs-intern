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