user_input = input("Enter a list of numbers separated by spaces: ")
input_list = user_input.split()
numbers = [int(num) for num in input_list]
corent_list = numbers[::]
reversed_list = numbers[::-1]
print("Corent List:", corent_list)
print("Reversed List:", reversed_list)