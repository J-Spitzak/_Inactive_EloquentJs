import random

def p1():
    print("what is " + str(random.randint(1,10)) + " * " + str(random.randint(1,10)) + "?")

def p2():
    print(int(input("add 2 numbers together \nnumber1:")) + int(input("number2:")))

def p3():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    print("what's", n1, "times",n2, "?")
    input()

def p4():
    x = random.randint(1,10)
    for _ in range(5):
        print(x)

def p5():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    print("what's", n1, "times",n2, "?")
    input()
    print(n1 * n2)

def p6():
    num = int(input())
    if num >= 100:
        print("big")
    else:
        print("little")

def p7():
    num = int(input())
    if num == 100:
        print("the number is 100")

def p8():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    print("what's", n1, "times",n2, "?")
    input_num = input()
    if int(input_num) == n1 * n2:
        print("YES!")
    else:
        print("NO!")

def p9_p1():
    for _ in range(3):
        win1 = random.randint(1, 10)
        win2 = random.randint(11, 20)
        win3 = random.randint(21, 30)

        winners = str(win1) + " " + str(win2) + " " + str(win3)

        print("And the three lucky winners are: " + winners + ".")

def p9_p2():
    for _ in range(10):
        n1 = random.randint(1,10)
        n2 = random.randint(1,10)

        print("what's", n1, "times",n2, "?")
        input_num = input()
        if int(input_num) == n1 * n2:
            print("YES!")
        else:
            print("NO!")

def p10():
    count = 0
    for _ in range(10):
        n1 = random.randint(1,10)
        n2 = random.randint(1,10)

        print("what's", n1, "times",n2, "?")
        input_num = input()
        if int(input_num) == n1 * n2:
            print("YES!")
            count += 1
        else:
            print("NO!")
    print("I asked you 10 questions.  You got " + str(count) + " of them right.")
    print("Well done!")