# Problem 8: Find the sum of the numbers passed as parameters using a function.

def sum_parameters(*args):
    return sum(args)

user_input = input("Enter numbers separated by space: ")  # e.g., "5 10 15 20"
numbers = [int(x) for x in user_input.split()]

result = sum_parameters(*numbers)
print("The sum of the numbers is:", result)
