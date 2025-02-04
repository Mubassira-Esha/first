# Problem 4: Find the second highest number from a set of numbers.
# Sample Input (when prompted): 10 20 4 45 99 45 20
# Expected Output:
#   The second highest number is: 45

user_input = input("Enter numbers separated by space: ")  # e.g., "10 20 4 45 99 45 20"
numbers = [int(x) for x in user_input.split()]

# Remove duplicates for distinct values.
unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Not enough distinct numbers to determine a second highest.")
else:
    unique_numbers.sort()
    second_highest = unique_numbers[-2]
    print("The second highest number is:", second_highest)
