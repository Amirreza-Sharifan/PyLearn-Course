print("Welcometo the Sorted or not Sorted program")
user_list = []
while 1==1:
    user = input("Please enter your number for adding to your list or type exit: ")
    if user == "exit":
        break
    else:
        user = float(user)
        user_list.append(user)

is_sorted = True

for i in range(1, len(user_list)):
    if user_list[i] < user_list[i - 1]:
        is_sorted = False
        break

if is_sorted == True:
    print("Your list is sorted from smallest to largest.")
else:
    print("Your list is not sorted.")

print(user_list)