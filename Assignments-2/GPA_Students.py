print("Welcome to the calculating of your GPA")
total_score = 0
counter = 0

while 1==1:
    score = input("Enter your score or 'exit' to calculate GPA: ")
    
    if score == "exit":
        break
    else:
        score = float(score)
        total_score += score
        counter += 1

average = total_score / counter
print("your GPA is:", average)