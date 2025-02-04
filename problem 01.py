# Problem 1: Sum of odd and even numbers from a set of numbers

user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)
