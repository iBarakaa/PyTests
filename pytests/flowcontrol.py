def eat(food):
    print("Thank you for the meal")

eat("chicken")


def flowIf(): 
    name = "Alice"
    if name == "Alice":
        print("Hi, Alice")
    print("done")

flowIf()

# loop control (for input validation)
def flowWhile():
    spam = 0
    while spam < 5:
        print(spam)
        spam = spam + 1

    print("boom!!!")

flowWhile()
    
#jumps execution to next
def whileContinue():
    spam = 0 
    while spam < 5:
        spam = spam + 1 
        if spam == 3:
            continue
        print("spam is " + str(spam))

whileContinue()


#infinity loop
def whileInfinity():
    name = ''
    while True:
        print("Please type your name: ")
        name = input()
        if name == "Kyomuu":
            # useful to exit loops
            break
    print("Welcome back!")

whileInfinity()

