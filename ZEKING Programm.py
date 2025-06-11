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
    print("Calculator -- 'cal' ")
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
        for question in range(1,2,1):
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
            print("Ammallarni Kiriting((a + b * 2) / 2 ** 3 ")
            print("x ** y  --> x - son, y - daraja")
            print("")
            a = input()
            b = a.split()
            c = len(b)
            d = int(b[0] + b[2])
            print(b,c,d)
            print("")
            print("Qayta foydalanish -- 'ENTER'. Menuga qaytish -- 'menu' ")
            action = input()
            if not action == "menu":
                continue
            else:
                break
        
        
        

                        #Aylana Uzunligi
                
    elif action == "cir":
        print("-" * 120)
        while True:
            r = int(input("Aylana Radiusini Kiriting!"))
            pi = 3.14
            uzun = 2*pi*r
            print("Aylananing Uzunligi -- ", uzun)
            print("-" * 120)                 
            continue

                        #Daraja
        
    elif action == "pow":
        print("-" * 120)
        while True:
            print("Sonni Kiriitng        *MENUga Qaytish -- '0' ")
            a = int(input())
            print("Darajani Kiriting")
            b = int(input())
            c = a**b
            print(a, "ning", b, "- darajasi -- ", c)
            print("-" * 120)
            continue

                        #Taqqoslash
        
    elif action == "taq":
        print("-" * 120)
        while True:
            print("Sonlarni Kiriting! ('a b c ... n' --> shu korinishda yozing.")
            a = input()
            b = a.split()
            if b[0] > b[1]:
                print(b[0],">",b[1])
            else:
                print(b[0],"<",b[1])








            
