import random
count = 0

for _ in range(10):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    print("what's", n1, "times",n2, "?")
    input_num = input()
    if input_num == "quit":
        break
    elif int(input_num) == n1 * n2:
        print("That’s right – well done.")
        count += 1
    else:
        print("No, I’m afraid the answer is " + str(n1*n2) + ".")
print("I asked you 10 questions, you got", count, "of them right")



