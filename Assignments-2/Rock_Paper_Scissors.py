import random
computer_score = 0
user_score = 0
while 1==1:
    x = random.randint(1,3)
    if x==1:
        computer_choice = "rock"
    elif x==2:
        computer_choice = "paper"
    elif x==3:
        computer_choice = "scissors"
    user_choice = input("Tyipe your choice: ")
    if user_choice == "exit":
        break
    print("💻:",computer_choice)
    if computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score + 1

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score + 1

    elif computer_choice == "rock" and user_choice == "paper":
        user_score = user_score + 1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score + 1

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score + 1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score + 1

    elif computer_choice == "paper" and user_choice == "paper":
        computer_score = computer_score + 0
        user_score = user_score + 0

    elif computer_choice == "rock" and user_choice == "rock":
        computer_score = computer_score + 0
        user_score = user_score + 0

    elif computer_choice == "scissors" and user_choice == "scissors":
        computer_score = computer_score + 0
        user_score = user_score + 0

print("Score of 💻:",computer_score)
print("Score of 👤:",user_score)