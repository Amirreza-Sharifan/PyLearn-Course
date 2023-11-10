num = int(input("Please enter your number for cheking the factorial: "))
if num < 0:
    print("Please enter the posetive number")
elif num == 0 or num == 1:
    print("yes")
else:
    factorial = 1
    i = 1
    while factorial < num:
        i += 1
        factorial *= i
    if factorial == num:
        print("Yes ✅")
    else:
        print("No ❌")
