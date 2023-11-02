import random
print("Hello and welcome to the mini 'Hang man' game.")
print("in this game you should guess a random word and be carefule because you have 'olny 6 guess'")
print("so lets begin 😎")
world_bank = ["black", "ali", "woman", "amirreza", "mashhad", "sharifan", "iran", "qormesabzi", "darya"]
mistake_user = 0
good_choice = []
bad_choice = []
word = random.choice(world_bank)
while mistake_user < 6:
    for i in range(len(word)):
        if word[i] in good_choice:
            print(word[i], end = " ")
        else:
            print("-", end =" ")
    if set(word) <= set(good_choice):
        print("🥳👏")
        break
    user_choice = input("Please enter your guess: ")
    if len(user_choice) == 1:
        if user_choice.lower() in word:
            good_choice.append(user_choice)
            print("✅")
        else:
            print("❌")
            bad_choice.append(user_choice)
            mistake_user += 1
    else:
        print("Please enter only one character ❗❗")
if mistake_user == 6:
    print("Game Over")
    print("💀💀💀")