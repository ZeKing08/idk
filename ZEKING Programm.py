import time
import random

print("Welcome!")
name = input("Please enter your name: ")
action = "menu"
print("-"*120,end="\n")

while action == "menu":
    print("MENU            ",name,end="\n")            #MENU
    print("Mathematical test -- 'test' ",end="\n")
    print("Calculator (demo) -- 'cal' ",end="\n")
    print("Length of circle -- 'len' ",end="\n")
    print("Power of -- 'pow' ",end="\n")
    print("Comparison -- 'comp' ",end="\n")
    action = input()
    
                            #Math Test
    if action == "math":
        print("-" * 120)
        print("")
        question = 1
        score = 0
        for question in range(1,2):
            a = random.randint(1,10)
            b = random.randint(10,30)
            q = random.randint(1,10)
            c = random.randint(5,15)
            d = random.randint(1,5)
            print("-" * 120)
            print("Question ",question,"/10",end="\n")
            ans = a * b * c * d
            user_ans = int(input(f"{a} * {b} * {c} * {d} = "))
            if user_ans == ans:
                score += 1
                print("Correct!   + 1",end="\n"); print("Your Score: ",score)
            else:
                print("Incorrect!  - 1",end="\n"); print("Your Score: ",score)
        print("Your result:",end="\n");print(f"Correct answers: {cor_ans} | Incorrect answers: {ins_ans} | Time: {time} | ")
        action = "menu"
        print("-" * 120)
        
                            #Kalkulator

                                        
    elif action == "cal":
        while True:
            print("-" * 120)
            print("Error")
            action = "menu"
            break
                        #Aylana Uzunligi
                
    elif action == "cir":
        print("-" * 120)
        while True:
            r = int(input("Enter radius: "))
            pi = 3.14
            uzun = 2*pi*r
            print("Length of circle is -- ", uzun)
            print("-" * 120)                 
            continue

                        #Daraja
        
    elif action == "pow":
        print("-" * 120)
        while True:
            print("Enter:    e.g. (a b)")
            a,b=map(int,input().split())
            print(f"{a} to the power of {b} is {a**b}")
            print("-" * 120)
            continue

                        #Taqqoslash
        
    elif action == "comp":
        print("-" * 120)
        while True:
            print("Enter the numbers      e.g: (a b)")
            a,b=map(int,inpur().split())
            if a>b:
                print(f"{a}>{b}")
            if a<b:
                print(f"{a}<{b}")
            else:
                print(f"{a}={b}")
