import random
print("Wlcome to the random list how you want")
print('the list will be made in range of [1-100]')
list = []
number = int(input("So just enter the n: "))
for i in range(number):
    x = random.randint(1, 100)
    list.append(x)
print(list)