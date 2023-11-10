user_input = input("Enter a list of numbers separated by spaces: ")
input_list = user_input.split()
numbers = [int(num) for num in input_list]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("List with unique elements:", unique_list)