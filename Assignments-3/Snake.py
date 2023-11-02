import random
print("Wlcome to the making snake program")
while 1==1:
    list = []
    user = input("Please enter your number for length of your snake or type exit: ")
    if user == "exit":
        break
    else:
        user = int(user)
    for i in range(user):
        x = random.randint(1, 100)
        list.append(x)
    counter = True
    for i in range(len(list)):
        if counter == True :
            print("*", end="")
        else:
            print("#", end="")
        counter = not counter
    print("🐍")