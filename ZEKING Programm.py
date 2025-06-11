print("Welcome!")
name = input("Please enter your name: ")
action = "menu"
print("-"*120)
print("")

while action == "menu":
    print("MENU            ",name,)      #MENU
    print("")
    print("Mathematical test -- 'test' ")
    print("")
    print("Calculator (demo) -- 'cal' ")
    print("")
    print("Length of circle -- 'len' ")
    print("")
    print("Power of -- 'pow' ")
    print("")
    print("Comparison -- 'comp' ")
    print("")
    action = input()
    
                            #Matem Test
    if action == "math":
        print("-" * 120)
        print("")
        import random
        question = 1
        score = 0
        for question in range(1,2):
            a = random.randint(1,10)
            b = random.randint(10,30)
            q = random.randint(1,10)
            c = random.randint(5,15)
            d = random.randint(1,5)
            print("-" * 120)
            print("Questian ",question,"/10")
            print("")
            ans = a * b * c * d
            print(a," * ",b," * ",c," * ",d," = ?")
            ur_ans = int(input())
            if ur_ans == ans:
                score = score + 1
                print("Correct!   + 1")
                print("Your Score: ",score)
            else:
                print("Incorrect!  - 1")
                print("Your Score: ",score)
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








            
