import random
print("Welcome to the Dice game")
print("in this game you should enter the special word (Roll)")
print("after enter Roll we will see the number of your Dice")
print("or you can enter (exit) for getting out of the game")
while 1==1:
    enter = (input("So Now Enter the (Roll) or (exit): "))
    if enter == "exit":
        break

    if enter == "Roll":
        dice = random.randint(1,6)
        if dice == 1:
            print("your chance is: 1️⃣")
        if dice == 2:
            print("your chance is: 2️⃣")
        if dice == 3:
            print("your chance is: 3️⃣")
        if dice == 4:
            print("your chance is: 4️⃣")
        if dice == 5:
            print("your chance is: 5️⃣")
        while dice == 6:
            print("your chance is: 6️⃣")
            print("you win, and your prise is:")
            dice = random.randint(1,6)
            if dice == 1:
                print("1️⃣")
            if dice == 2:
                print("2️⃣")
            if dice == 3:
                print("3️⃣")
            if dice == 4:
                print("4️⃣")
            if dice == 5:
                print("5️⃣")
            if dice == 6:
                print("6️⃣")
    else:
        print("Check your spell and try again")