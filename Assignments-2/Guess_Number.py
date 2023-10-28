import random
print("Welcome to the - Guess Number game -")
print("in this game you should guess a number between [1,100]")
print("after you find a number I'll tell you about the number of your steps")
computer_num = random.randint(1, 100)
counter = 0
while 1==1:
    counter = counter + 1
    user_num = int(input("Now what is your guess?: "))
    if computer_num == user_num:
        break
    elif computer_num < user_num:
        print("Go down")
        print("🔽")
    else:
        print("Go up")
        print("🔼")
print("well done, It is true👏")
print("the random number was:",computer_num, ",and your all steps to find it is:" ,counter)