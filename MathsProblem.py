import random
import time

min_operand = 1
max_operand = 15
hardOprators = ["+", "-", "/", "*"]
mediumOperators= ["+", "-", "*"]
easyOperators = ["+", "-"]

wrong = 0

def problemGenrator():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    oprator = random.choice(hardOprators)
    while left<right:
        left = random.randint(min_operand, max_operand)
        right = random.randint(min_operand, max_operand)

    exr = str(left)+oprator+str(right) 
    answer = eval(exr)
    return(exr, answer)

def easyProblemGenrator():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    oprator = random.choice(easyOperators)
    while left<right:
        left = random.randint(min_operand, max_operand)
        right = random.randint(min_operand, max_operand)

    exr = str(left)+oprator+str(right) 
    answer = eval(exr)
    return(exr, answer)

def mediumProblemGenrator():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    oprator = random.choice(mediumOperators)
    while left<right:
        left = random.randint(min_operand, max_operand)
        right = random.randint(min_operand, max_operand)

    exr = str(left)+oprator+str(right) 
    answer = eval(exr)
    return(exr, answer)


while True:
    number_of_ques = int(input("How many questions you want? "))
    q = input("Ready? (y/n?)")
    startTime = time.time()
    if q == "y":
        for i in range(number_of_ques):
            expr, answer = problemGenrator()
            while True:
                guess = input(f"#{i+1}. {expr} = ")
                if guess == str(answer):
                    print("Correct Answer!\n")
                    break
                elif guess == "s":
                    expr, answer = problemGenrator()
                elif guess != str(answer):
                    print("Wrong Answer")
                    print(f"Corrent Answer: {answer}\n")
                    wrong=+1
                    expr, answer = problemGenrator()
                    break
        endTIme = time.time()
        final = endTIme-startTime
        correct = 10-wrong
        print(f"Correct Answers: {int(correct)}")
        print(f"You did it in {int(final)} Seconds")
        o = input("\nWanna play again? ")
        if o == "y":
            break
        else:
            exit()
    elif q=="n":
        break

