# Problem 2: Find the smallest number from a set of numbers

# Input numbers separated by space.
user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

if numbers:  # Check if the list is not empty
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print("The smallest number is:", smallest)
else:
    print("No numbers entered!")
