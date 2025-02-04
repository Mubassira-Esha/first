# Problem 7: Find the largest number between two numbers using a function.

def largest_of_two(a, b):
    return a if a > b else b

num1 = int(input("Enter the first number: "))   # e.g., 15
num2 = int(input("Enter the second number: "))  # e.g., 42

print("The largest number between", num1, "and", num2, "is:", largest_of_two(num1, num2))
