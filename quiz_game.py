print("Welcome to QuizWhiz🎯")

score = 0
attempted = 0

q1 = q2 = q3 = q4 = q5 = q6 = q7 = False

while True:
    print("\n🧠 QUIZ MENU")
    print("1. Do pigeons have ears?")
    print("2. Is tomato a fruit?")
    print("3. Do sharks blink?")
    print("4. Do octopuses have 3 hearts?")
    print("5. Is the sun a planet?")
    print("6. Can bats see in complete darkness?")
    print("7. Is water made of hydrogen and oxygen?")
    print("8. Show Score")
    print("9. Exit")

    choice = input("Choose a question: ")

    # Q1
    if choice == "1" and not q1:
        ans = input("Do pigeons have ears? ").lower()
        attempted += 1
        q1 = True
        if ans == "yes":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q2
    elif choice == "2" and not q2:
        ans = input("Is tomato a fruit? ").lower()
        attempted += 1
        q2 = True
        if ans == "yes":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q3
    elif choice == "3" and not q3:
        ans = input("Do sharks blink? ").lower()
        attempted += 1
        q3 = True
        if ans == "no":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q4
    elif choice == "4" and not q4:
        ans = input("Do octopuses have 3 hearts? ").lower()
        attempted += 1
        q4 = True
        if ans == "yes":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q5
    elif choice == "5" and not q5:
        ans = input("Is the sun a planet? ").lower()
        attempted += 1
        q5 = True
        if ans == "no":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q6
    elif choice == "6" and not q6:
        ans = input("Can bats see in complete darkness? ").lower()
        attempted += 1
        q6 = True
        if ans == "no":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    # Q7
    elif choice == "7" and not q7:
        ans = input("Is water made of hydrogen and oxygen? ").lower()
        attempted += 1
        q7 = True
        if ans == "yes":
            print("Correct 😎")
            score += 1
        else:
            print("Bruh 😭")

    elif choice == "8":
        print("Score:", score, "/", attempted, "🏆")

    elif choice == "9":
        if attempted < 5:
            print("⚠️ Attempt at least 5 questions before exiting!")
        else:
            print("Final Score:", score, "/", attempted, "Attempted🎯:")
            break

    else:
        print("Invalid or already attempted 👀")
