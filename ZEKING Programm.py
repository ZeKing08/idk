import time
import random

print("Welcome!")
name = input("Please enter your name: ")
print("-" * 120)

while True:
    print(f"\nMENU - {name}")
    print("Mathematical test -- 'test'")
    print("Calculator (demo) -- 'cal'")
    print("Length of circle -- 'len'")
    print("Power of -- 'pow'")
    print("Comparison -- 'comp'")
    print("Exit -- 'exit'")

    action = input("Choose an option: ").strip().lower()
    print("-" * 120)

    if action == "test":
        cor_ans = 0
        inc_ans = 0
        start_time = time.perf_counter()

        for question in range(1, 11):
            a = random.randint(1, 10)
            b = random.randint(10, 30)
            c = random.randint(5, 15)
            d = random.randint(1, 5)
            ans = a * b * c * d
            print(f"Question {question}/10")
            try:
                user_ans = int(input(f"{a} * {b} * {c} * {d} = "))
                if user_ans == ans:
                    cor_ans += 1
                    print("Correct!\n")
                else:
                    inc_ans += 1
                    print("Incorrect!\n")
            except ValueError:
                inc_ans += 1
                print("Invalid input. Counted as incorrect.\n")

        timer = round(time.perf_counter() - start_time, 2)
        print("\nYour result:")
        print(f"Correct: {cor_ans} ({cor_ans*10}%) | Incorrect: {inc_ans} | Time: {timer} seconds")
        print("-" * 120)

    elif action == "cal":
        print("Calculator is currently in demo mode (not implemented).")
        print("-" * 120)

    elif action == "len":
        try:
            r = float(input("Enter radius: "))
            uzun = round(2 * 3.14 * r, 2)
            print(f"Length of circle: {uzun}")
        except ValueError:
            print("Invalid radius input.")
        print("-" * 120)

    elif action == "pow":
        try:
            a, b = map(int, input("Enter two numbers (e.g. 2 5): ").split())
            print(f"{a} ** {b} = {a**b}")
        except ValueError:
            print("Invalid input.")
        print("-" * 120)

    elif action == "comp":
        try:
            a, b = map(int, input("Enter two numbers (e.g. 7 3): ").split())
            if a > b:
                print(f"{a} > {b}")
            elif a < b:
                print(f"{a} < {b}")
            else:
                print(f"{a} = {b}")
        except ValueError:
            print("Invalid input.")
        print("-" * 120)

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Unknown command. Try again.")
